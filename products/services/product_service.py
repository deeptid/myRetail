from products.models import ProductItem


class ProductService(object):
    def getAllProducts(self):
        return ProductItem.objects.filter(isDeleted=False)

    def getByProductId(self, productId):
        return ProductItem.objects.filter(productId=productId)

    def getByProductIds(self, productIds):
        return ProductItem.objects.filter(productId__in=productIds, isDeleted=False)

    def getById(self, id):
        return ProductItem.objects.get(id=id)
