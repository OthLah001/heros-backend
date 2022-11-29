from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Hero

class ListHerosSerializer(ModelSerializer):
    userId = IntegerField(source='user.id')

    class Meta:
        model = Hero
        fields = ['userId', 'name', 'powers']