from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookListApiTests(APITestCase):

    def setUp(self):
        # Создаем несколько тестовых книг для использования в тестах
        self.book1 = Book.objects.create(name='Book 1', author='Author 1', publish_year='2020-10-10', isbn=1)
        self.book2 = Book.objects.create(name='Book 2', author='Author 2', publish_year='2021-10-10', isbn=1)
        self.book3 = Book.objects.create(name='Book 3', author='Author 3', publish_year='2022-10-10', isbn=1)
        self.url = 'book-list'

    def test_list_books(self):
        # Проверяем, что эндпоинт списка книг возвращает код 200
        url = reverse(self.url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что все три тестовые книги присутствуют в ответе
        self.assertEqual(len(response.data), 3)

    def test_search_books(self):
        # Проверяем, что эндпоинт поиска возвращает код 200
        url = reverse(self.url)
        response = self.client.get(url, {'search': 'Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе только одна книга, соответствующая поисковому запросу
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_order_books(self):
        # Проверяем, что эндпоинт сортировки возвращает код 200
        url = reverse(self.url)
        response = self.client.get(url, {'ordering': 'publish_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что книги упорядочены по году выпуска в порядке возрастания
        years = [book['publish_year'] for book in response.data]
        self.assertEqual(years, ['2020-10-10', '2021-10-10', '2022-10-10'])
