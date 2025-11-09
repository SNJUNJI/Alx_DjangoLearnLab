from django.contrib import admin
from .models import Book  # Import your model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields as columns in the list view
    list_display = ['title', 'author', 'publication_year']
    
    # Add filters in the sidebar (e.g., dropdowns for author and publication_year)
    list_filter = ['author', 'publication_year']
    
    # Enable search box for these fields
    search_fields = ['title', 'author']
    
    # Optional: Make title editable inline in the list view for quick changes
    list_editable = ['title']
    
    # Optional: Set a human-readable title for the admin page
    verbose_name_plural = "Books"  # Overrides the auto-pluralization if needed
