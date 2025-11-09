from django.urls import path
from .views import list_books  # Exact line to match
from .views import LibraryDetailView  # Add if needed for specificity

urlpatterns = [
    path('books/', list_books, name='book_list'),  # Uses direct import
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
