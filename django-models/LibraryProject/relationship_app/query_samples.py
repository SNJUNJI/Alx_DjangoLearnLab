from relationship_app import models
book=Book.object.get()

all_books=Book.object.all()
print (all_books)

librarian=library.object.get(name="Library")
print (librarian)