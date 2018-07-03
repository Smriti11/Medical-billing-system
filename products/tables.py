import django_tables2 as tables
from .models import Products

class ProductTable(tables.Table):
    class Meta:
        model = Products
        exclude = ['prod_cost']
        template_name = 'django_tables2/bootstrap.html'
