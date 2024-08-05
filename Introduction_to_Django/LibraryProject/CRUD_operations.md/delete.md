### Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

<!-- The book instance is deleted from the database. -->