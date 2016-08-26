from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from checkout.models import Order, OrderItem
from accounts.forms import UserProfileForm
from accounts import profile

def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username','')
            pw = postdata.get('password1')
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request,new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    return render(request,'registration/register.html',locals())

@login_required
def my_account(request):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    return render(request,'registration/my_account.html', locals())

def order_info(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = 'Edit Order Information'
    return render(request,'registration/order_info.html',locals())

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = 'Order Details for Order # ' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'registration/order_details.html', locals())

