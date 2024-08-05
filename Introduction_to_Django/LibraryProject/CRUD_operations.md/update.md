### Update Operation

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

<!-- The title of the book is updated to "Nineteen Eighty-Four". -->