from django.contrib import admin
from .models import Book

# Define the custom admin class
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view (title, author, publication_year)
    list_display = ['title', 'author', 'publication_year']
    
    # Sidebar filters for usability (e.g., by author or publication year)
    list_filter = ['author', 'publication_year']
    
    # Search capabilities (query by title or author)
    search_fields = ['title', 'author']
    

# Register using your original syntax
admin.site.register(Book, BookAdmin)