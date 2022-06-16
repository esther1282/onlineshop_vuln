from datetime import datetime
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=750)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

def product_image_path(instance, filename):
    return 'static/images/shop/{}'.format(filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    num = models.IntegerField(default=1)
    image = models.ImageField(upload_to=product_image_path)

    def __str__(self):
        return self.product.name + "'s images"