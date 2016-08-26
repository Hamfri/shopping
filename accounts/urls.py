#from django.conf.urls.defaults import *
from django.conf.urls import url
from shopping import settings
from accounts import views


urlpatterns = [
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$','django.contrib.auth.views.login', name='login'),
    url(r'^my_account/$',views.my_account, name='my_account'),
    url(r'^order_details/(?P<order_id>[-\w]+)/$',views.order_details,name='order_details'),
    url(r'^order_info/$',views.order_info, name='order_info'),
]