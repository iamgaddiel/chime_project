from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from inventory.models import Product, Sale, Supplier



class Dashboard(TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.all().count()
        context['total_sales'] = Sale.objects.all().count()
        context['total_suppliers'] = Supplier.objects.all().count()
        return context
