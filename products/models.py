from django.db import models

# Create your models here.

class Product(models.Model):
    """Product SKU(integer)
    Brand name(string)
    Product slug(string)
    Product title(string)
    Quantity(integer)"""

    product_SKU = models.IntegerField(unique=True)
    brand_name = models.CharField(max_length=127)
    product_slug = models.CharField(max_length=127)
    product_title = models.CharField(max_length=127)
    quantity = models.IntegerField(default=0)

