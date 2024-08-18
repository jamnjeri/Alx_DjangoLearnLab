# Query All Books by a Specific Author:
from .models import Author, Book

author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)

# List All Books in a Library:
from .models import Library

library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

# Retrieve the Librarian for a Library:
from .models import Library, Librarian

library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)

print(librarian.name)