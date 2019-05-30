from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home,name ='home'),
    url(r'^signup',views.signup, name='signup'),
    url(r'^index', views.index, name = 'index'),
    url(r'user/(?P<username>\w+)', views.profile,name='profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^image/(?P<image_id>\d+)', views.single_image, name='single_image'),
    url(r'^search/', views.search, name='search')
]