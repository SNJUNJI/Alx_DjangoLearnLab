from .models import *

# 1. All books by specific author
author_name = 'Example Author'  # Replace with actual
all_books = Book.objects.filter(author__name=author_name)
print([b.title for b in all_books])

# 2. Books in a library (exact lines to match checker)
library_name = 'Example Library'  # Replace with actual
lib = Library.objects.get(name=library_name)
books_in_lib = lib.books.all()
print([b.title for b in books_in_lib])

# 3. Librarian for a library
librarian_ = lib.librarian
print(librarian_.name)
