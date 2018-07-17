from django.conf.urls import  url
from .import views

urlpatterns = [
        url(r'^supplier/$',views.supplier,name='supplier'),
        url(r'^supplier/(?P<id>[0-9]+)/update/$', views.supplier_update, name='supplier_update'),
        url(r'^supplier/(?P<id>[0-9]+)/delete/$',views.supplier_delete,name='supplier_delete'),
        url(r'^addsupplier/', views.addsupplier, name='addsupplier'),


        ]
