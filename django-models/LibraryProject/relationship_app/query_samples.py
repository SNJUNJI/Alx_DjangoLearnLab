from .models import *

# 1. All books by specific author
author_name = 'Example Author'  # Replace with actual
author = Author.objects.get(name=author_name)
all_books = Book.objects.filter(author=author)
print([b.title for b in all_books])

# 2. Books in a library
library_name = 'Example Library'  # Replace
lib = Library.objects.get(name=library_name)
books_in_lib = lib.books.all()
print([b.title for b in books_in_lib])

# 3. Librarian for a library (exact to match: Librarian.objects.get(library=...)
librarian_ = Librarian.objects.get(library=lib)
print(librarian_.name)
