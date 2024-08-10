### Create Operation

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) <Book: Book object (1)>

```python
from bookshelf.models import Book
new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()
print(new_book)
```

<!--  Expected Output: -->
<!--  A new Book instance is created and saved to the database. -->
<!--  1984 is printed to the console. -->
