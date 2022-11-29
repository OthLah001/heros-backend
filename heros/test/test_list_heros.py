from django.test import TestCase
from ..models import Hero
from users.models import AppUser
from rest_framework import status
import json

class TestAddHero(TestCase):
    fixtures = ["users", "heros"]

    def setUp(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": user.email, "password": "test1234"})
        result = json.loads(response.content)
        self.token = result['token']

    def test_get_list_heros_with_correct_params(self):
        response = self.client.get(f'/heros/list/{self.token}/', { "page": 1, "orderBy": "name" })
        result = json.loads(response.content)
        
        self.assertEqual(result["count"], 7)
        self.assertEqual(result["previous"], None)
        self.assertEqual(len(result["results"]), 3)

    def test_get_list_heros_with_wrong_page(self):
        response = self.client.get(f'/heros/list/{self.token}/', { "page": 999, "orderBy": "name" })
        
        self.assertEqual(response.status_code, 404)

    def test_get_list_heros_with_wrong_orderBy(self):
        response = self.client.get(f'/heros/list/{self.token}/', { "page": 1, "orderBy": "wrong" })
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)