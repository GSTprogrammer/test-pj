from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import CustomUser

class SignupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Testpass123!",
            "user_type": "client"
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 1)
