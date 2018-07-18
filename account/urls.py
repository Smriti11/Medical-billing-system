from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^home/', views.home, name='home'),
    url(r'^logout/',auth_views.logout,{'next_page':'/login'},name='logout'),

]
