from django.shortcuts import render
from relationship_app.models import Book

# Create your views here.
def list_books(request, *args, **kwargs):
    books=Book.objects.get()
    return render(request, "list_books.html",{books})