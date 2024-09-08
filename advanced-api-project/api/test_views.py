from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name="Jennifer Lynn Barnes")
        self.book1 = Book.objects.create(title="The Inheritance Games", publication_year=2021, author=self.author)
        self.book2 = Book.objects.create(title="Restore Me", publication_year=2018, author=self.author)
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Book Title',
            'publication_year': 2022,
            'author': self.author.id,
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book Title',
            'publication_year': 2022,
            'author': self.author.id,
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2021,
            'author': self.author.id,
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_order_books(self):
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.data[0]['title'], 'Restore Me')

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'The Inheritance Games'})
        self.assertEqual(response.data[0]['author'], 1)
