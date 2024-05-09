from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.shortcuts import resolve_url, redirect
from django.contrib import messages

from .models import Product, Supplier, Sale
from .forms import ProductCreateForm, SupplierCreationForm, SaleCreationForm, SaleUpdateForm, SupplierUpdateForm

from core.utils import generate_random_string

from core.models import Record

class AddProduct(CreateView):
    """Create/Adds Product to Database """
    model = Product
    form_class = ProductCreateForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:product_list')
    
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        SKU = 'SKU-' + generate_random_string(5)
        form.instance.sku = SKU
        form.instance.sold = 0
        res = form.save()
        Record(
            action='ADD_PRODUCT',
            ref_id=res.id,
            record_type='Product'
        ).save()
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
    model = Supplier
    form_class = SupplierCreationForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:supplier_list')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        supplier_id = 'SP-' + generate_random_string(5)
        form.instance.supplier_id = supplier_id
        form_instance = form.save()
        Record(
            action='ADD_SUPPLIER',
            ref_id=form_instance.id,
            record_type='Supplier'
        ).save()
        return super().form_valid(form)


class UpdateSupplierDetails(UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:supplier_list')

class ListSupplier(ListView):
    model = Supplier
    

def delete_supplier(request, pk):
    try:
        Supplier.objects.get(id=pk).delete()
    except Supplier.DoesNotExist:
        template_name = 'inventory/supplier_list.html'
        context = {
            "object_list": Supplier.objects.all(),
            "err_msg": "Invalid supplier"
        }
        return render(request, template_name, context)
    
    return resolve_url('core:inventory:supplier_list')


# Sales
class ListsSale(ListView):
    model = Sale

class CreateSales(CreateView):
    model = Sale
    form_class = SaleCreationForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:sale_list')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        try:
            # Create Sale TransactionID
            sale_id = 'SP-' + generate_random_string(5)
            form.instance.sale_id = sale_id
            form.instance.transaction_status = 'pending'
            
            
            form_quantity = form.instance.quantity
            product = Product.objects.get(title=form.instance.item)
            product_current_quantity = product.quantity
            
            # insufficient product quantity
            if product_current_quantity < form_quantity:
                messages.error(self.request, 'Insufficient product quantity')
                return redirect('core:inventory:sale_create')
            
            # incorrect price paid
            amount_to_be_paid = form_quantity * product.price
            if form.instance.paid != amount_to_be_paid:
                messages.error(self.request, 'Incorrect amount, correct amount should be {0}'.format(amount_to_be_paid))
                return redirect('core:inventory:sale_create')
            
            # Update Product Quantity
            new_product_quantity = product_current_quantity - form_quantity
            product.quantity = new_product_quantity
            product.save()
            
            # Create Record
            form_instance = form.save()
            Record(
                action='CREATE_SALE_TRANSACTION',
                ref_id=form_instance.id,
                record_type='Sale'
            ).save()
            
        except Product.DoesNotExist:
            messages.error(self.request, 'Wrong item selected')
            return redirect('core:inventory:sale_create')
        
        return super().form_valid(form)
    
    
class SalesUpdateView(UpdateView):
    model = Sale
    form_class = SaleUpdateForm
    
    def get_success_url(self) -> str:
        return resolve_url('core:inventory:sale_list')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form_instance = form.save()
        Record(
            action='UPDATE_SALE_TRANSACTION',
            ref_id=form_instance.id,
            record_type='Sale'
        ).save()
        return super().form_valid(form)