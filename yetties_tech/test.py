import os

from django.test import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yetties_tech.settings')

from django.contrib.auth.models import User
from django.urls import reverse


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_valid_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'mypassword123',
            'password2': 'mypassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_invalid_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'mypassword123',
            'password2': 'differentpassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    # User Login and Logout Tests
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='mypassword123')

    def test_valid_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'mypassword123',
        })
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='testuser', password='mypassword123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)
