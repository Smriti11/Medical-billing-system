from django.db import models

# Create your models here.

class Products(models.Model):
    prod_name= models.CharField(max_length=100,unique=True, verbose_name='product name',blank=True)
    prod_code= models.IntegerField(unique=True,verbose_name='product code',blank=True)
    prod_price= models.DecimalField(max_digits=17, decimal_places=2,verbose_name='product price',blank=True)
    prod_category= models.CharField(max_length=100,verbose_name='product category',blank=True)
    prod_description= models.TextField(max_length=500,verbose_name='product description',blank=True)
    prod_quantity= models.IntegerField(verbose_name='product quantity',blank=True)
    prod_discount= models.DecimalField(max_digits=17, decimal_places=2,verbose_name='product discount',blank=True)
    prod_tax=models.DecimalField(max_digits=17, decimal_places=2,verbose_name='product tax',blank=True)
    prod_cost=models.DecimalField(max_digits=17, decimal_places=2,verbose_name='product cost',blank=True)


    def __str__(self):
        return self.prod_name
