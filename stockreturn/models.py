from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Stockreturn(models.Model):
    product_id=models.IntegerField()
    bill_no=models.IntegerField()
    supplier_id=models.IntegerField()
    supplier_name=models.CharField(max_length=30)
    supplier_contact=models.IntegerField()


    def __str__(self):
        return self.supplier_name
