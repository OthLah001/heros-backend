from django.test import TestCase
from ..models import AppUser
import json

class TestSignUp(TestCase):
    fixtures = ["users"]
    test_email = "test@test.com"

    def test_create_new_account_with_correct_data(self):
        newUser = {
            "email": self.test_email,
            "password": "test1234",
            "firstName": "Elon",
            "lastName": "Musk"
        }
        response = self.client.post('/users/signup/', data=newUser)
        result = json.loads(response.content)

        user = AppUser.objects.all().order_by('creation_date').last()

        self.assertEqual(result['user']['firstName'], newUser['firstName'])
        self.assertEqual(user.email, newUser['email'])

    def test_create_new_account_with_existing_email(self):
        user = AppUser.objects.all().first()
        newUser = {
            "email": user.email,
            "password": "test1234",
            "firstName": "Elon",
            "lastName": "Musk"
        }
        response = self.client.post('/users/signup/', data=newUser)
        result = json.loads(response.content)

        self.assertEqual(result, { "detail": "User already exists" })

