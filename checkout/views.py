from django.shortcuts import render
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from .forms import CheckoutForm
from .models import Order, OrderItem
import checkout
from cart import cart
from accounts import profile

def show_checkout(request):
    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            response = checkout.process(request)
            order_number = response.get('order_number',0)
            error_message = response.get('message','')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = "Correct the errors below"
                
    elif request.user.is_authenticated():
            user_profile = profile.retrieve(request)
            form = CheckoutForm(instance=user_profile)
    else:
        form = CheckoutForm()
    page_title = 'Checkout'
    return render(request,'checkout/checkout.html',locals())

def receipt(request):
    order_number = request.session.get('order_number','')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    return render(request,'checkout/receipt.html',locals())
        





