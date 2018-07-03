from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'medsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^products/', include('products.urls')),

]
