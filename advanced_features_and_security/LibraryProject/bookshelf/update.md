### Update Operation
book.title = "Nineteen Eighty-Four" {'_state': <django.db.models.base.ModelState object at 0x0000015EDF36E310>, 'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

<!-- The title of the book is updated to "Nineteen Eighty-Four". -->