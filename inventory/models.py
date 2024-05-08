from django.db import models
from uuid import uuid4



class Product(models.Model):
    category = [
        ("Clothes", "Clothes"),
        ("Cosmetics", "Cosmetic"),
        ("Laptop", "Laptop"),
        ("Mobile", "Mobile"),
        ("Gaming accessories", "Gaming accessories"),
    ]
    
    STATUS = [
        ('available', 'available'),
        ('low', 'low'),
        ('out_of_stock', 'out_of_stock'),
    ]
    
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, blank=True)
    description = models.CharField(max_length=40, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    category = models.CharField(max_length=18, choices=category)
    min_low_threshold_quantity = models.IntegerField(help_text='The minium quantity reached before product is considered low in inventory')
    sold = models.IntegerField(default=0)
    status = models.CharField(max_length=12, default=STATUS[0])
    sku = models.CharField(max_length=10)
    created_at = models.DateField(auto_now=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    def get_current_items_in_stock(self):
        return self.quantity - self.sold


class Supplier(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    supplier_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    item = models.CharField(max_length=10)
    phone = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    tax_number = models.CharField(max_length=10, unique=True)
    
    def __str__(self) -> str:
        return f'{self.name} | {self.phone}'
    

class Sale(models.Model):
    STATUS = {
        'pending': 'Pending',
        'completed': 'Completed',
        'declined': 'Declined',
    }
    
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    sale_id = models.CharField(max_length=20)
    buyer_name = models.CharField(max_length=20)
    supplier = models.ForeignKey(to=Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    transaction_status = models.CharField(max_length=14, choices=STATUS)
    quantity = models.IntegerField()
    paid = models.BigIntegerField()
    created_at = models.DateField(auto_now=True)
    
