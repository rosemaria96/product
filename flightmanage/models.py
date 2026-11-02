from django.db import models

# Create your models here.

class Flight(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=100)
    price = models.IntegerField(max_length=100)
    def __str__(self):
        return self.product_name

