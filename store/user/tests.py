from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import CustomUser


class CustomUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('user-registration'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'testuser')

    def test_create_user_missing_required_fields(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('user-registration'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)
