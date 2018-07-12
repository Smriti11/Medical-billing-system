import django_tables2 as tables
from .models import Supplier

class SupplyTable(tables.Table):
    class Meta:
        model = Supplier
        template_name = 'django_tables2/bootstrap.html'
