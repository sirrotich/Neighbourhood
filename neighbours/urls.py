from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home,name ='home'),
    url(r'^index', views.index, name = 'index'),
]