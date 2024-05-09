from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Product, Supplier, Sale


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
        
        
class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['supplier_id']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Grace Peters'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'email@example.com'
            }),
            'item': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Samsung Phone'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1234567890'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'No 123 Ave.'
            }),
            'tax_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '345678987'
            }),
        }


class SaleCreationForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['sale_id', 'transaction_status']
        widgets = {
            'buyer_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Name of buyer'
            }),
            'quantity' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': '10,000',
                'type': 'number',
                'min': 1
            }),
            'paid' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': '1000000',
                'type': 'number',
                'min': 1
            }),
            'supplier': forms.Select(attrs={
                'class' : 'form-control',
            }),
            'item': forms.Select(attrs={
                'class' : 'form-control',
            }),
        }
        

class SaleUpdateForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['transaction_status']
        widgets = {
            'transaction_status': forms.Select(attrs={
                'class' : 'form-control',
            })
        }