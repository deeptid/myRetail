import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

class JSONField(models.TextField):
    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value

# Looking at the Json, Why price is not part of item
class ProductItem(models.Model):
    productId = models.IntegerField(db_index=True, unique=True)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(null=True)
    formattedPrice = models.CharField(max_length=50)
    buyUrl = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    metaData = JSONField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)


