from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.show_checkout,name='checkout'),
    url(r'^receipt/$',views.receipt,name='checkout_receipt'),
]
