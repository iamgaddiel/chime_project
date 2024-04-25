from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import resolve_url
from core.utils import generate_random_string

from .models import Product, Supplier
from .forms import ProductCreateForm, SupplierCreationForm


class AddProduct(CreateView):
    """Create/Adds Product to Database """
    model = Product
    form_class = ProductCreateForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:product_list')
    
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        SKU = 'SKU-' + generate_random_string(5)
        form.instance.sku = SKU
        return super().form_valid(form)


class ListProduct(ListView):
    model = Product
    

class ProductDetail(DetailView):
    model = Product
    
    
def delete_product(request):
    """ Delete a single instance of Product from the database"""
    return

def search_products(request):
    """ Search for product title containing request string"""
    return 



# Suppliers
class CreateSupplier(CreateView):
    """Create/Adds Supplier to Database """
    model = Supplier
    form_class = SupplierCreationForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:supplier_list')
    
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        supplier_id = 'SP-' + generate_random_string(5)
        form.instance.supplier_id = supplier_id
        return super().form_valid(form)


class ListSupplier(ListView):
    model = Supplier