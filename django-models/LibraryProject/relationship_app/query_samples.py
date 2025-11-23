from relationship_app.models import Book, Librarian, Library, Author
book=Book.object.filter(author=Author)

library=Library.objects.get(name="Library")
all_books=library.objects.all()
print(all_books)

librarian=Library.object.get(name=Library_name), books.all()
print (librarian)