import json
import urllib.request

from django.http import HttpResponse
from django.shortcuts import render
from products.models import ProductItem
from products.services.parser import Parser
from products.services.product_service import ProductService

BASE_URL = "https://redsky.target.com/v2/pdp/tcin/"


def saveProductDetail(data):

    products = []
    productItem = ProductItem(
        productId=data.getValueOf('product.available_to_promise_network.product_id'),
        title=data.getValueOf('product.item.product_description.title'),
        description=data.getValueOf('product.item.product_description.downstream_description'),
        formattedPrice='$' + str(data.getValueOf('product.price.listPrice.price')),
        imageUrl=data.getValueOf('product.item.enrichment.images[0].base_url') + data.getValueOf('product.item.enrichment.images[0].primary'),
        item_type=data.getValueOf('product.item.product_classification.item_type_name'),
        product_type=data.getValueOf('product.item.product_classification.product_type_name'),
    )
    print("data:{}".format(data.getValueOf('product')))
    productItem.metaData = data.getValueOf('product')
    productItem.save()
    products.append(productItem)
    return products 



def index(request):
    products = []
    productId = request.GET.get('product_id')
    if productId and productId != '':
        productInDB = ProductService().getByProductId(productId)
        if not productInDB:
            try:
                url = BASE_URL + str(productId) + "?excludes=taxonomy,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics"
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())
                if data and data.get('product').get('item'):
                    productResponse = Parser(data)
                    products = saveProductDetail(productResponse)
                else:
                    return HttpResponse("Empty Response")
            except Exception:
                return render(request, 'shop/index.html', {'response': False})
        else:
            if productInDB.last().isDeleted:
                return render(request, 'shop/index.html', {'isDeleted': True})
            products = productInDB

    return render(request,'shop/index.html', {'products': products, 'response': True})


def detail(request, productId):
    productItem = ProductService().getByProductId(productId).last()
    productItem.metaData = str(productItem.metaData)
    return render(request,'shop/detail.html', {'product_item': productItem})


def item(request):
    return HttpResponse("Item")


def rawData(request, productId):
    productItem = ProductService().getByProductId(productId).last()
    rawData = productItem.metaData
    return render(request, 'shop/raw_data.html', {'raw_data': rawData})

def edit(request, productId):
    productItem = ProductService().getByProductId(productId).last()
    if request.method == "POST":
        print("request.POST:{}".format(request.POST))
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        formattedPrice = request.POST.get("formattedPrice", "")
        item_type = request.POST.get("item_type", "")
        product_type = request.POST.get("product_type", "")

        # save data
        productItem.title = title
        productItem.description = description
        productItem.formattedPrice = formattedPrice
        productItem.item_type = item_type
        productItem.product_type = product_type

        productItem.save()

    return render(request, 'shop/edit.html', {'productItem': productItem})


def delete(request, productId):
    productItem = ProductService().getByProductId(productId).last()
    productItem.isDeleted = True
    productItem.save()
    return render(request, 'shop/index.html', {'isDeleted': True})
