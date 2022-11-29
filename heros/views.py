from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Hero
from backend.common import IsAuthenticate, AppPagination
from rest_framework.generics import ListAPIView
from .serializers import ListHerosSerializer
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