from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Supplier(models.Model):
    supplier_name=models.CharField(max_length=30)
    supplier_contact=models.IntegerField()
    supplier_address=models.CharField(max_length=30)
    supplier_description=RichTextField()


    def __str__(self):
        return self.supplier_name
