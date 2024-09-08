# DOCUMENTATIONS

## Filtering
- Parameters: title, author, publication_year
- Usage: GET /api/books/?title=some_title&author=some_author

## Searching
- Parameters: search
- Usage: GET /api/books/?search=some_keyword

## Ordering
- Parameters: ordering
- Usage: GET /api/books/?ordering=title or GET /api/books/?ordering=-publication_year