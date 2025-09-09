from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import *
from .form import *
from django.urls import reverse_lazy
from django.urls import reverse
import django_filters
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# BOOK

class CreateBOOK(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'Library/create_book.html'
    success_url = reverse_lazy('Library:book_list')


class BookListView(ListView):
    model = Book
    template_name = "Library/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "Library/book_detail.html"
    context_object_name = "book" 

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "Library/update_book.html"
    
    def get_success_url(self):
        return reverse("Library:book_detail", kwargs={"pk": self.object.pk})


class BookDeleteView(DeleteView):
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
            Q(category__name__icontains=value) |  
            Q(price__icontains=value)
        )

def Book_Filter(request):
    filter = BooktFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'Library/Book_Filter.html', {'filter': filter , 'books': filter.qs})



# CATEGORY
class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Library/create_category.html'
    success_url = reverse_lazy('Library:book_list')


class CategoryListView(ListView):
    model = Category
    template_name = "Library/category_list.html"
    context_object_name = "categories"


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "Library/update_category.html"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "Library/delete_category.html"
    success_url = reverse_lazy("category_list")


# BORROWING
class CreateBorrowing(CreateView):
    model = Borrowing
    form_class = BorrowingForm
    template_name = 'Library/create_borrowing.html'
    success_url = reverse_lazy('borrowing_list')


class BorrowingListView(ListView):
    model = Borrowing
    template_name = "Library/borrowing_list.html"
    context_object_name = "borrowings"


class BorrowingDetailView(DetailView):
    model = Borrowing
    template_name = "Library/borrowing_detail.html"


class BorrowingUpdateView(UpdateView):
    model = Borrowing
    form_class = BorrowingForm
    template_name = "Library/update_borrowing.html"
    success_url = reverse_lazy("borrowing_list")


class BorrowingDeleteView(DeleteView):
    model = Borrowing
    template_name = "Library/delete_borrowing.html"
    success_url = reverse_lazy("borrowing_list")
