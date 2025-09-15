from django import forms
from .models import *

class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
            
            
class BookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title','author','description','category','price','copies_available','pdf' , 'image'
        ]
    
class BorrowingForm (forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = []
    