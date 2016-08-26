import random
from django.core import urlresolvers

from cart import cart
from .models import Order, OrderItem
from .forms import CheckoutForm
from accounts import profile


def get_checkout(request):
    return urlresolvers.reverse('checkout')

def _generate_transaction_id(request):
    transaction_id = ''
    characters = '0123456789'
    transaction_id_length = 7
    for n in range(transaction_id_length):
        transaction_id += characters[random.randint(0,len(characters)-1)]
    return transaction_id
    
    

def process(request):
    postdata = request.POST.copy()
    results = {}
    transaction_id = _generate_transaction_id(request)
    order = create_order(request,transaction_id)
    #amount = cart.cart_subtotal(request)
    results = {'order_number':order.id,}
    return results

def create_order(request,transaction_id):
    order = Order()
    checkout_form = CheckoutForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()
    # if the order save succeeded
    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            # create order item for each cart item
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()
        #all set, empty cart
        cart.empty_cart(request)
        # save profile info for future orders
        if request.user.is_authenticated():
            profile.set(request)
        # return the new order object
    return order
    
    
    
    
    
    