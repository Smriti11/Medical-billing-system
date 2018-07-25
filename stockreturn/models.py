from django.db import models
from django.contrib.auth.models import User
from products.models import Products
from supplier.models import Supplier
# Create your models here.
class Stockreturn(models.Model):
    product_id=models.ForeignKey(Products)
    bill_no=models.IntegerField()
    supplier_id=models.ForeignKey(Supplier)
    supplier_contact=models.IntegerField()


    def __str__(self):
        return self.supplier_id
