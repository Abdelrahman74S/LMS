from django.db import models
from account.models import MyUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60 , blank=False, null=False)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=60 , blank=False, null=False)
    author = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(blank=False, null=False ,default='No description yet')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    copies_available = models.IntegerField(blank=False, null=False)
    pdf = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to="")
    
    def __str__(self):
        return self.title
    
class Borrowing(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrower = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField()
    
    STATUS_CHOICES = [
    ('borrowed', 'Borrowed'),
    ('returned', 'Returned'),
    ('late', 'Late'),
]
    status = models.CharField(max_length=20, choices= STATUS_CHOICES ,default='borrowed')
    
    def __str__(self):
            return f"{self.borrower.username} borrowed {self.book.title}"