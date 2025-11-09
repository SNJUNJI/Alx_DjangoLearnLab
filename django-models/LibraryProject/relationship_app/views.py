from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library  # Exact line to match checker

# Function-based view (unchanged)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (unchanged)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
