from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView ,DetailView, ListView
from .models import *
from .form import *
from django.urls import reverse_lazy
from django.urls import reverse
import django_filters
from django.db.models import Q , F
from django.db import transaction
from django.utils import timezone 
from datetime import timedelta 
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth.mixins import UserPassesTestMixin ,LoginRequiredMixin


class SallerUserPassesTestMixin (UserPassesTestMixin):
    def test_func(self):
       return self.request.user.is_authenticated and self.request.user.account_type == 'seller' 
   
# BOOK    
class CreateBOOK(SallerUserPassesTestMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'Library/create_book.html'
    success_url = reverse_lazy('Library:book_list')
    

class BookListView(ListView):
    model = Book
    template_name = "Library/book_list.html"
    context_object_name = "books"


class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    template_name = "Library/book_detail.html"
    context_object_name = "book" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            has_borrowed = Borrowing.objects.filter(
                book=self.object,               
                borrower=self.request.user,      
                return_date__isnull=True       
            ).exists() 

            context['user_has_borrowed_book'] = has_borrowed
        else:
            context['user_has_borrowed_book'] = False
            
        return context

class BookUpdateView(SallerUserPassesTestMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = "Library/update_book.html"
    
    def get_success_url(self):
        return reverse("Library:book_detail", kwargs={"pk": self.object.pk})

class BookDeleteView(SallerUserPassesTestMixin,DeleteView):
    model = Book
    success_url = reverse_lazy("Library:book_list")

class BooktFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', label="Search")

 
    class Meta:
        model = Book
        fields = [] 

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(author__icontains=value) |
            Q(category__name__icontains=value) 
        )

def Book_Filter(request):
    filter = BooktFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'Library/Book_Filter.html', {'filter': filter , 'books': filter.qs})


# CATEGORY
class CreateCategory(SallerUserPassesTestMixin,CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Library/create_category.html'
    success_url = reverse_lazy('Library:category_list')
    
    
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = "Library/category_list.html"
    context_object_name = "categories"


class CategoryUpdateView(SallerUserPassesTestMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "Library/update_category.html"
    success_url = reverse_lazy("Library:category_list")
    context_object_name = "category" 


class CategoryDeleteView(SallerUserPassesTestMixin,DeleteView):
    model = Category
    template_name = "Library/delete_category.html"
    success_url = reverse_lazy("Library:category_list")
    context_object_name = "category" 
    
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('Library:category_list')
    return render(request, 'Library/delete_category.html', {'category': category})


# BORROWING
@login_required(login_url='account:login')
@permission_required('Library.add_borrowing', raise_exception=True)
def create_borrowing(request, book_pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_pk)
        borrower = request.user

        if Borrowing.objects.filter(book=book, borrower=borrower, return_date__isnull=True).exists():
            return redirect('Library:book_detail', pk=book_pk)
        
        try:
            with transaction.atomic():
                book_to_update = Book.objects.select_for_update().get(pk=book.pk)
                
                if book_to_update.copies_available > 0:
                    Borrowing.objects.create(
                        book=book,
                        borrower=borrower,
                        due_date=timezone.now() + timedelta(days=14)
                    )
                    Book.objects.filter(pk=book.pk).update(copies_available=F('copies_available') - 1)
                    return redirect('Library:borrowing_list')
                else:
                    return redirect('Library:book_detail', pk=book_pk)
        except Exception as e:
            return redirect('Library:book_detail', pk=book_pk)

    return redirect('Library:book_list')


class BorrowingListView(LoginRequiredMixin,ListView):
    model = Borrowing
    template_name = "Library/borrowing_list.html"
    context_object_name = "borrowings"
    
    def get_queryset(self):
        user = self.request.user
        if user.account_type == 'seller':
            
            return Borrowing.objects.all()
        else:
            return Borrowing.objects.filter(borrower=user)

@login_required(login_url='account:login')
def BookRetrieval( request,  pk):
    borrowing = Borrowing.objects.get(pk=pk)
    book = borrowing.book

    with transaction.atomic():
        Book.objects.filter(pk=book.pk).update(copies_available=F('copies_available') + 1)
        borrowing.return_date = timezone.now()
        borrowing.save()
        
    return redirect('Library:borrowing_list')


