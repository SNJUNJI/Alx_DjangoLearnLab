from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # Fixed: Added max_length and ()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title  # Fixed: Use title, not name
    
    class Meta:
        # Custom permissions for add/edit/delete (in addition to Django defaults)
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)  # Fixed: Added max_length
    books = models.ManyToManyField(Book)  # Fixed: Plural for clarity
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Fixed: Added max_length
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name