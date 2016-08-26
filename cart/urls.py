from django.conf.urls import include, url
#from cart import views

urlpatterns = [
    url(r'^$', 'cart.views.show_cart', name='show_cart'),
]
