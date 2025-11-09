from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book, Library

# Existing views (unchanged)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# New: Custom LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# New: Registration View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

# New: Custom LogoutView (renders template on success)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
