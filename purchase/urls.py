from django.conf.urls import  url
from .import views

urlpatterns = [
        url(r'^purchase/',views.purchase,name='purchase'),
        url(r'^addpurchase/', views.addpurchase, name='addpurchase'),
        url(r'^purchase/(?P<id>[0-9]+)/update/$',views.purchase_update,name='purchase_update'),

        ]
