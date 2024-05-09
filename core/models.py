from django.db import models
from uuid import uuid4

# Create your models here.


ACTIONS = [
    ('ADD_PRODUCT', 'ADD_PRODUCT'),
    ('ADD_SUPPLIER', 'ADD_SUPPLIER'),
    ('CREATE_SALE_TRANSACTION', 'CREATE_SALE_TRANSACTION'),
    ('UPDATE_SALE_TRANSACTION', 'UPDATE_SALE_TRANSACTION'),
]    

    
class Record(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    action = models.CharField(max_length=23, choices=ACTIONS)
    ref_id = models.CharField(max_length=200)
    record_type = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True, null=True)
    
    def __str__(self) -> str:
        return '{0} ->  {1}'.format(self.action, self.ref_id)
    
