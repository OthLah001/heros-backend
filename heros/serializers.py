from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField
from .models import Hero, Rating

class ListHerosSerializer(ModelSerializer):
    userId = IntegerField(source='user.id')
    rating = SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Hero
        fields = ['userId', 'id', 'name', 'powers', 'rating']

    def get_rating(self, obj):
        rating_qs = Rating.objects.filter(hero=obj, user=self.user).first()
        return rating_qs.rating if rating_qs else 0

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'description', 'powers']