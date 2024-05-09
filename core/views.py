from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Record

from inventory.models import Product, Sale, Supplier



class Dashboard(TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.all().count()
        context['total_sales'] = Sale.objects.all().count()
        context['total_suppliers'] = Supplier.objects.all().count()
        context['transactions'] = Sale.objects.all().reverse()[:3]
        return context


class RecordList(ListView):
    model = Record


class RecordDetail(TemplateView):
    template_name = 'core/record_detail.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        record_type = kwargs.get('record_type')
        ref_id = kwargs.get('ref_id')
        action = kwargs.get('action')
        
        # ADD_PRODUCT
        if record_type == 'Product':
            product = Product.objects.get(id=ref_id)
            context['object'] = product
            
        if record_type == 'Supplier':
            supplier = Supplier.objects.get(id=ref_id)
            context['object'] = supplier
            
        if record_type == 'Sale':
            sales = Sale.objects.get(id=ref_id)
            context['object'] = sales
            
            
        context['record_type'] = record_type
        context['action'] = action
        return context