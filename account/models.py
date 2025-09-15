from django.db import models 
from django.contrib.auth.models import AbstractUser  , Group

class MyUser(AbstractUser): 
    phone_number = models.CharField(max_length=11, blank=False, null=False) 
    address = models.CharField(max_length=100, blank=False, null=False) 
    MyPhoto = models.ImageField(upload_to="MyPhoto/", null=True, blank=True)
    
    ACCOUNT_TYPES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    ]
    
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES , default='customer')
    
    def save(self, *args, **kwargs):
         # Before getting ID
         is_new = self.pk is None

         # After obtaining the ID   
         super().save(*args, **kwargs)
         if is_new:
            if self.account_type == 'customer':
               group = Group.objects.get_or_create(name='Customers')
               self.groups.add(group)
            elif self.account_type == 'seller':
                group = Group.objects.get_or_create(name='Sellers')
                self.groups.add(group)

    def __str__(self): 
        return self.username 