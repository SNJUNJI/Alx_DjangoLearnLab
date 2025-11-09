#blank
from .models import Author Book Library Librarian

specific_Author='Sam'
books=Author.object.filter(Author__name=specific_Author)
print([b.title for b in books])



