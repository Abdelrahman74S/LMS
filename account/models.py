from django.db import models 
from django.contrib.auth.models import AbstractUser 

class MyUser(AbstractUser): 
    phone_number = models.CharField(max_length=11, blank=False, null=False) 
    address = models.CharField(max_length=100, blank=False, null=False) 
    
    def __str__(self): return self.username