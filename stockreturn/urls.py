from django.conf.urls import  url
from .import views


urlpatterns = [
        url(r'^stockreturn/$',views.stockreturn,name='stockreturn'),



        ]
