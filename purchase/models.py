from django.db import models
from django.contrib.auth.models import User
from products.models import Products
from supplier.models import Supplier


# Create your models here.

class Purchase(models.Model):
        prod_id=models.ForeignKey(Products)
        currrent_stock=models.IntegerField()
        purchase_date=models.DateField()
        supplier=models.ForeignKey(Supplier)
        quantity=models.IntegerField()
        tax_rate=models.IntegerField()
        discount=models.IntegerField()



        def __str__(self):
            return self.prod_id
