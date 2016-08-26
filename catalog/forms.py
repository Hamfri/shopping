from django import forms

from catalog.models import Category, Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug','brand','sku','price','old_price',\
                  'is_active','is_bestseller','is_featured','quantity',\
                  'description','meta_keywords','meta_description', \
                  'categories','image','thumbnail','image_caption']
    
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']