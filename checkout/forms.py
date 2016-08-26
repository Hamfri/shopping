import re
import datetime
from django import forms
from .models import Order

def strip_non_numbers(data):
    "get rid of all non number characters"
    non_numbers = re.compile('\D')
    return non_numbers.sub('',data)

class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        #override default attributes
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '30'
        self.fields['shipping_state'].widget.attrs['size'] = '3'
        self.fields['shipping_country'].widget.attrs['size'] = '3'
        self.fields['shipping_zip'].widget.attrs['size'] = '6'
        self.fields['billing_state'].widget.attrs['size'] = '3'
        self.fields['billing_country'].widget.attrs['size'] = '3'
        self.fields['billing_zip'].widget.attrs['size'] = '6'
    class Meta:
        model = Order
        exclude = ['status','ip_address','user','transaction_id',]
    
    def clean_phone(self):
        phone =self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone)<10:
            raise forms.ValidationError('Enter a valid phone number(eg 072x-xxxxxx)')
        return self.cleaned_data['phone']
