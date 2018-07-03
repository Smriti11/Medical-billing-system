from django.db import models

# Create your models here.

class Products(models.Model):
    prod_name= models.CharField(max_length=100,unique=True)
    prod_code= models.IntegerField(unique=True)
    prod_price= models.DecimalField(max_digits=17, decimal_places=2)
    prod_category= models.CharField(max_length=100)
    prod_description= models.TextField(max_length=500)
    prod_quantity= models.IntegerField()
    prod_discount= models.DecimalField(max_digits=17, decimal_places=2)
    prod_tax=models.DecimalField(max_digits=17, decimal_places=2)
    prod_cost=models.DecimalField(max_digits=17, decimal_places=2)

    def __str__(self):
        return self.prod_name
