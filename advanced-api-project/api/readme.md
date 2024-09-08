# Filtering, Searching and Ordering Documentation:

## Filtering
- Parameters: title, author, publication_year
- Usage: GET /api/books/?title=some_title&author=some_author

## Searching
- Parameters: search
- Usage: GET /api/books/?search=some_keyword

## Ordering
- Parameters: ordering
- Usage: GET /api/books/?ordering=title or GET /api/books/?ordering=-publication_year


# Testing Documentation:

## Overview

This documentation covers the testing approach and individual test cases for the Book API endpoints using Django REST Framework's APITestCase. The tests validate the functionality of listing, creating, updating, deleting, ordering, and searching books.

## Testing Strategy

The tests ensure that the Book API endpoints behave correctly under various scenarios, including authentication checks, CRUD operations, and query functionalities. The tests are designed to cover:
- Authentication and authorization
- CRUD operations (Create, Read, Update, Delete)
- Ordering and searching functionalities

## Test Cases

### Test Case 1: test_list_books

*Objective*: Verify that the GET /books/ endpoint correctly retrieves a list of books.

*Steps*:
1. Send a GET request to the list_url.
2. Assert that the response status code is 200 OK.
3. Assert that the number of books in the response data is 2.

*Expected Result*: The response should have a status code of 200 OK and contain two books.

### Test Case 2: test_create_book

*Objective*: Verify that an authenticated user can create a new book.

*Steps*:
1. Log in with username='testuser' and password='testpassword'.
2. Send a POST request to the create_url with the new book data.
3. Assert that the response status code is 201 Created.

*Expected Result*: The new book should be successfully created, and the response status code should be 201 Created.

### Test Case 3: test_create_book_unauthenticated

*Objective*: Verify that an unauthenticated user cannot create a new book.

*Steps*:
1. Send a POST request to the create_url with the new book data without logging in.
2. Assert that the response status code is 403 Forbidden.

*Expected Result*: The request should be forbidden for unauthenticated users, and the response status code should be 403 Forbidden.

### Test Case 4: test_update_book

*Objective*: Verify that an authenticated user can update an existing book.

*Steps*:
1. Log in with username='testuser' and password='testpassword'.
2. Send a PUT request to the update_url with updated book data.
3. Assert that the response status code is 200 OK.

*Expected Result*: The existing book should be updated successfully, and the response status code should be 200 OK.

### Test Case 5: test_delete_book

*Objective*: Verify that an authenticated user can delete an existing book.

*Steps*:
1. Log in with username='testuser' and password='testpassword'.
2. Send a DELETE request to the delete_url.
3. Assert that the response status code is 204 No Content.

*Expected Result*: The book should be deleted successfully, and the response status code should be 204 No Content.

### Test Case 6: test_order_books

*Objective*: Verify that books can be ordered by a specified field.

*Steps*:
1. Send a GET request to the list_url with an ordering parameter (ordering=title).
2. Assert that the first book in the response data has the title 'Restore Me'.

*Expected Result*: Books should be ordered by title, with 'Restore Me' being the first in the list.

### Test Case 7: test_search_books

*Objective*: Verify that books can be searched by a specified query.

*Steps*:
1. Send a GET request to the list_url with a search parameter (search=The Inheritance Games).
2. Assert that the first book in the response data has the author ID 1.

*Expected Result*: The response should include the book 'The Inheritance Games', and its author ID should be 1.

## Running the Tests

To run the tests, use Django's test runner with the following command:

```bash
python manage.py test
```

The above command will discover and execute all test cases defined in the test file (test_views.py)