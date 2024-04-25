from django import forms

from .models import Product, Supplier


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['sku']
        
        
class SupplierCreationForm(forms.ModelForm):
    class Meta:
        model = Supplier
        # fields = '__all__'
        exclude = ['supplier_id']


