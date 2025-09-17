from django.contrib import admin
from .models import Book, Category , Borrowing
from account.models import MyUser
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Borrowing)  