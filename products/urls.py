from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^products-list/', views.products, name='products'),
    url(r'^pos/', views.pos, name='pos'),
    url(r'^addproduct/', views.addproduct, name='addproduct'),

]
