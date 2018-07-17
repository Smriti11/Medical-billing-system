from django.conf.urls import  url
from .import views


urlpatterns = [
        url(r'^stockreturn/$',views.stockreturn,name='stockreturn'),
        url(r'^addstockreturn/', views.addstockreturn, name='addstockreturn'),
        url(r'^stockreturn/(?P<id>[0-9]+)/update/$',views.stockreturn_update,name='stockreturn_update'),
        url(r'^stockreturn/(?P<id>[0-9]+)/delete/$',views.stockreturn_delete,name='stockreturn_delete'),



        ]
