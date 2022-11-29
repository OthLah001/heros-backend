from django.test import TestCase
from ..models import Hero, Rating
from users.models import AppUser
from rest_framework import status
import json

class TestAddHero(TestCase):
    fixtures = ["users", "heros"]

    def setUp(self):
        self.user = AppUser.objects.all().first()
        response = self.client.post('/users/login/', data={"email": self.user.email, "password": "test1234"})
        result = json.loads(response.content)
        self.token = result['token']

    def test_rate_hero_with_different_user(self):
        hero = Hero.objects.exclude(user=self.user).first()
        response = self.client.post(f'/heros/rate/{self.token}/', data={"heroId": hero.id, "rating": 4})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rating.objects.get(hero=hero, user=self.user).rating, 4)

    def test_rate_hero_with_same_user(self):
        hero = Hero.objects.filter(user=self.user).first()
        response = self.client.post(f'/heros/rate/{self.token}/', data={"heroId": hero.id, "rating": 4})
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)