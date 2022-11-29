from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Hero
from backend.common import IsAuthenticate

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