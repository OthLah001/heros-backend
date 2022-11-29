from django.test import TestCase
from ..models import Hero
from users.models import AppUser
from rest_framework import status
import json

class TestAddHero(TestCase):
    fixtures = ["users"]
    hero = {
        "name": "Batman",
        "description": "Rich man with black suit",
        "powers": "Rich, Strong, Energy"
    }

    def setUp(self):
        user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": user.email, "password": "test1234"})
        result = json.loads(response.content)
        self.token = result['token']


    def test_add_hero_with_coorrect_data(self):
        response = self.client.post(f'/heros/add/{self.token}/', data=self.hero)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hero.objects.all().count(), 1)
        self.assertEqual(Hero.objects.first().name, self.hero["name"])

    def test_add_hero_with_wrong_user(self):
        response = self.client.post(f'/heros/add/_{self.token}_/', data=self.hero)
        
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Hero.objects.all().count(), 0)

    def test_add_hero_without_name_or_powers(self):
        self.hero["name"] = ""
        response = self.client.post(f'/heros/add/{self.token}/', data=self.hero)

        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(Hero.objects.all().count(), 0)