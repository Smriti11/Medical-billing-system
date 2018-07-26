from django.db import models
from django.contrib.auth.models import User
#from supplier .models import Supplier

# Create your models here.

class Purchase(models.Model):
        prod_code=models.IntegerField()
        product_name=models.CharField(max_length=30, blank = 'True')
        product_price=models.IntegerField()
        currrent_stock=models.IntegerField()
        purchase_date=models.DateField()
        supplier=models.CharField(max_length = 30, blank = 'True')
        quantity=models.IntegerField()
        tax_rate=models.IntegerField()
        discount=models.IntegerField()


        def __str__(self):
            return self.product_name
