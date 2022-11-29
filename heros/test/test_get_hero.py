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

    def test_get_hero_with_correct_id(self):
        hero = Hero.objects.all().first()
        response = self.client.get(f'/heros/get/{hero.id}/{self.token}/')
        result = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["name"], hero.name)
        self.assertEqual(result["description"], hero.description)
        self.assertEqual(result["powers"], hero.powers)

    def test_get_hero_with_wrong_id(self):
        response = self.client.get(f'/heros/get/999/{self.token}/')
        self.assertEqual(response.status_code, 404)
