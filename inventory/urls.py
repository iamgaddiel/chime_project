from django.urls import path

from .views import (
    AddProduct,
    delete_product,
    ListProduct,
    search_products,
    ProductDetail,
    ListSupplier,
    CreateSupplier
)


app_name = 'inventory'

urlpatterns = [
    path('', ListProduct.as_view(), name='product_list'),
    path('create/', AddProduct.as_view(), name='product_create'),
    path('product/delete/<uuid:product_id>/', delete_product, name='product_delete'),
    path('product/detail/<uuid:product_id>/', AddProduct.as_view(), name='product_detail'),
    
    # supplier
    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/add', CreateSupplier.as_view(), name='supplier_create'),
]
