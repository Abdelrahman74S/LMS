from django.db import models 
from django.contrib.auth.models import AbstractUser , Permission

class MyUser(AbstractUser): 
    phone_number = models.CharField(max_length=11, blank=False, null=False) 
    address = models.CharField(max_length=100, blank=False, null=False) 
    
    ACCOUNT_TYPES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    ]
    
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES , default='customer')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  

        if self.account_type == 'customer':
            perms = Permission.objects.filter(
                codename__in=['can_borrow_books', 'can_view_books']
            )
            self.user_permissions.set(perms)

        elif self.account_type == 'seller':
            perms = Permission.objects.filter(
                codename__in=['can_borrow_books', 'can_view_books','can_add_books', 'can_delete_books', 'can_update_books']
            )
            self.user_permissions.set(perms)

    def __str__(self): 
        return self.username

# class Customer(MyUser):
#     class Meta:
#         proxy = True
#         permissions = [
#           ('can_borrow_books' , 'Can borrow books'),
#           ('can_view_books' , 'Can view books'),
#         ]     
        
# class Seller(MyUser):
#     class Meta:
#         proxy = True
#         permissions = [
#           ('can_borrow_books' , 'Can borrow books'),
#           ('can_view_books' , 'Can view books'),
#           ('can_add_books' , 'Can add books'),
#           ('can_delete_books' , 'Can delete books'),
#           ('can_update_books' , 'Can update books'),
#         ]    