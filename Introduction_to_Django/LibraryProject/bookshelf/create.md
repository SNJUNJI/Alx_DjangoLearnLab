from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected: No output, but creation is successful (you can print(book) to verify)
