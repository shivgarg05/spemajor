from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework import serializers

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/api/auth/register', data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertTrue('user' in response.data)
        #self.assertTrue('token' in response.data)
        # You can perform additional assertions to validate the response data

class LoginAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = AuthToken.objects.create(self.user)[1]

    def test_login_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/api/auth/login', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertFalse('user' in response.data)
        #self.assertTrue('token' in response.data)
        # You can perform additional assertions to validate the response data

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = AuthToken.objects.create(self.user)[1]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_get_user(self):
        response = self.client.get('/api/auth/user')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertTrue('username' in response.data)
        #self.assertNotEqual(response.data['username'], 'testuser')
        # You can perform additional assertions to validate the response data

# Add more test cases as needed

class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        serializer = UserSerializer(user)
        expected_data = {
            'id': user.id,
            'username': 'testuser',
            'email': 'testuser@example.com'
        }
        self.assertEqual(serializer.data, expected_data)

class RegisterSerializerTest(TestCase):
    def test_register_serializer(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

class LoginSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_serializer_with_valid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        validated_user = serializer.validate(data)
        self.assertEqual(validated_user, self.user)

    def test_login_serializer_with_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'incorrectpassword'
        }
        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaisesMessage(serializers.ValidationError, "Incorrect Credentials"):
            validated_user = serializer.validate(data)
