from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products-list/$', views.products, name='products'),
    url(r'^addproduct/', views.addproduct, name='addproduct'),
    url(r'^products-list/(?P<id>[0-9]+)/update/$',views.products_update,name='products_update'),
    url(r'^products-list/(?P<id>[0-9]+)/delete/$',views.products_delete,name='products_delete'),

]
