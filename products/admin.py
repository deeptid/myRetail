from django.contrib import admin

# Register your models here.
from products.models import ProductItem

admin.site.register(ProductItem)