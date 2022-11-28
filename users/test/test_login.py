from django.test import TestCase
from ..models import AppUser
import json

class TestLogin(TestCase):
    fixtures = ["users"]

    def test_login_with_correct_data(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": user.email, "password": "test1234"})
        result = json.loads(response.content)
        
        self.assertEqual(result['user']['id'], user.id)
        self.assertEqual(result['user']['firstName'], user.first_name)
        self.assertEqual(result['user']['lastName'], user.last_name)

    def test_login_with_wrong_email(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": "wrong@wrong.wrong", "password": "test1234"})
        result = json.loads(response.content)
        
        self.assertEqual(result, {'detail': 'Not found.'})

    def test_login_with_wrong_password(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": user.email, "password": "wrong_password"})
        result = json.loads(response.content)
        
        self.assertEqual(result, { "detail": "User not found" })

class TestCheckToken(TestCase):
    fixtures = ["users"]

    def setUp(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": user.email, "password": "test1234"})
        result = json.loads(response.content)
        self.token = result['token']

    def test_check_token_with_correct_token(self):
        response = self.client.get(f'/users/check_token/{self.token}/')
        result = json.loads(response.content)
        
        self.assertEqual(result, { "message": "Token is ok" })

    def test_check_token_with_wrong_token(self):
        response = self.client.get(f'/users/check_token/_{self.token}_/')
        result = json.loads(response.content)
        
        self.assertEqual(result, { "message": "Token is wrong" })