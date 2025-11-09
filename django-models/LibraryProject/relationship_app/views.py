from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    text_list = "Books Available:\n"
    for book in books:
        text_list += f"- {book.title} by {book.author.name}\n"
    return HttpResponse(text_list, content_type='text/plain')

# Create your views here.
