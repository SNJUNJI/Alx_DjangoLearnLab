book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
# Confirm by querying all
all_books = Book.objects.all()
print(list(all_books))  # Expected: []
