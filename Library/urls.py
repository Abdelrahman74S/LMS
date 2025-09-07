from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Library"

urlpatterns = [
    # BOOK
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("create-book/", CreateBOOK.as_view(), name="create_book"),
    path("update-book/<int:pk>/", BookUpdateView.as_view(), name="update_book"),
    path("delete-book/<int:pk>/", BookDeleteView.as_view(), name="delete_book"),

    # CATEGORY
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path('create-category/', CreateCategory.as_view(), name='create_category'),
    path("update-category/<int:pk>/", CategoryUpdateView.as_view(), name="update_category"),
    path("delete-category/<int:pk>/", CategoryDeleteView.as_view(), name="delete_category"),

    # BORROWING
    path("borrowings/", BorrowingListView.as_view(), name="borrowing_list"),
    path("create-borrowing/", CreateBorrowing.as_view(), name="create_borrowing"),
    path("borrowing/<int:pk>/", BorrowingDetailView.as_view(), name="borrowing_detail"),
    path("update-borrowing/<int:pk>/", BorrowingUpdateView.as_view(), name="update_borrowing"),
    path("delete-borrowing/<int:pk>/", BorrowingDeleteView.as_view(), name="delete_borrowing"),
]

