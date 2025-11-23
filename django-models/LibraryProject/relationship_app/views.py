from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
def list_books(request, *args, **kwargs):
    books=Book.objects.all()
    return render(request, "relationship_app/list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    library=Library.objects.get(name="Library name")
    all_books=library.objects.all()
    for i in all_books:
        print (all_books)
    template_name="relationship_app/library_detail.html"