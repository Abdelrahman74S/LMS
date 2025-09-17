from django.db import models 
from django.contrib.auth.models import AbstractUser  , Group
from cloudinary.models import CloudinaryField

class MyUser(AbstractUser): 
    phone_number = models.CharField(max_length=11, blank=False, null=False) 
    address = models.CharField(max_length=100, blank=False, null=False) 
    MyPhoto = CloudinaryField('Myimage', resource_type="auto", blank=True, null=True)
    
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
               group = Group.objects.get(name='Customers')
               self.groups.add(group)
            elif self.account_type == 'seller':
                group = Group.objects.get(name='Sellers')
                self.groups.add(group)

    def __str__(self): 
        return self.username 