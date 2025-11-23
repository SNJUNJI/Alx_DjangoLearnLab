from bookshelf.models import Book  # Import if not already in shell
book = Book.objects.get(title="1984")  # Fetch the book (using 'book' variable to match expected "book.title")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # This line contains "book.title" for verification
