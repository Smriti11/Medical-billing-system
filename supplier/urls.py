from django.conf.urls import  url
from .import views

urlpatterns = [
        url(r'^supplier/',views.supplier,name='supplier'),


        ]
