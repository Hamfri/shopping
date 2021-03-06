from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id','cart_id','date_added','quantity','product']
    class Meta:
        model = CartItem

admin.site.register(CartItem, CartItemAdmin)
        
