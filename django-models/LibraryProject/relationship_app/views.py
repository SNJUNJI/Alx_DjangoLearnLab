from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Renamed to list_books
def list_books(request):  # Changed from book_list
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (unchanged)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
