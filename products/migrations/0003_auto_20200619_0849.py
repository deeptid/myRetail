# Generated by Django 3.0.7 on 2020-06-19 08:49

from django.db import migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productitem_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='metaData',
            field=products.models.JSONField(blank=True, null=True),
        ),
    ]