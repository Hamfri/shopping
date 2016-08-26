from django.conf.urls import include, url
from django.contrib import admin
from catalog import views

urlpatterns = [
    url(r'^$', views.index, name='catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, name='show_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, name='show_product'),
    
]
