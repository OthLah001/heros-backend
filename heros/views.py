from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Hero, Rating
from backend.common import IsAuthenticate, AppPagination
from rest_framework.generics import ListAPIView
from .serializers import ListHerosSerializer, HeroSerializer
from rest_framework.exceptions import APIException
from django.db.models import Q

class AddHeroView(APIView):
    permission_classes = [IsAuthenticate]

    def post(self, request, token):
        name = request.data["name"]
        description = request.data["description"]
        powers = request.data["powers"]

        if not name or not powers:
            return Response(
                { "message": "Not enough information." }, status=status.HTTP_406_NOT_ACCEPTABLE
            )

        Hero.objects.create(
            user=request.user, name=name, description=description, powers=powers
        )
        return Response(
            { "message": "Hero created successfully." }, status=status.HTTP_200_OK
        )

class ListHerosView(ListAPIView):
    permission_classes = [IsAuthenticate]
    serializer_class = ListHerosSerializer
    pagination_class = AppPagination

    class ListHeroException(APIException):
        status_code = status.HTTP_400_BAD_REQUEST
        default_detail = ""

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs["user"] = self.request.user
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy', 'name')
        search = self.request.query_params.get('search', None)
        heros_qs = Hero.objects.all()

        if search:
            heros_qs = heros_qs.filter(Q(name__icontains=search) | Q(powers__icontains=search))

        if orderBy not in ("name", "powers"):
            raise self.ListHeroException(detail="Invalid orderBy param")
        heros_qs = heros_qs.order_by(orderBy)

        return heros_qs

class HeroView(APIView):
    permission_classes = [IsAuthenticate]

    def get(self, request, id, token):
        hero = get_object_or_404(Hero, id=id)
        return Response(HeroSerializer(hero).data, status=status.HTTP_200_OK)

class HeroRatingView(APIView):
    permission_classes = [IsAuthenticate]

    class HeroRatingException(APIException):
        status_code = status.HTTP_400_BAD_REQUEST
        default_detail = ""

    def post(self, request, token):
        heroId = request.data["heroId"]
        rating = request.data["rating"]

        hero = get_object_or_404(Hero, id=heroId)
        if hero.user == request.user:
            raise self.HeroRatingException(detail="User can't rate his heros.")

        try:
            heroRating = Rating.objects.get(hero=hero, user=request.user)
        except:
            heroRating = Rating.objects.create(hero=hero, user=request.user, rating=0)

        heroRating.rating = rating
        heroRating.save()
        return Response({ "message": "Hero rated." }, status=status.HTTP_200_OK)
