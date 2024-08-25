### Delete Operation
from bookshelf.models import Book book.delete() bookshelf.models.Book.DoesNotExist: Book matching query does not exist.

But if it's in the terminal, you can use:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

<!-- The book instance is deleted from the database. -->