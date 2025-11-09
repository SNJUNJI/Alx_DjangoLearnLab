from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # From previous
from django.views.generic.detail import DetailView
from .models import Book, Library

# Existing views (unchanged)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# New: Function-based register (to match "views.register")
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)  # Logs in after register
            return redirect('book_list')  # Or 'login'
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
