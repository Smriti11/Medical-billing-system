from django.conf.urls import include, url
from django.contrib import admin
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'medsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^supplier/', include('supplier.urls')),
    url(r'^stockreturn/', include('stockreturn.urls')),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}, name='login'),
    url(r'^dash/$', views.dash, name='dash'),
    url(r'^super/$', views.super, name='super'),
    

]
