from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import AppUser
import jwt
import datetime
from django.conf import settings

class InitDataMixin():
    def _get_init_data(self, user):
        data = {}
        data['user'] = {
            "id": user.id,
            "email": user.email,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "lastLoggin": user.last_logged_in_date
        }
        return data

class InitView(APIView, InitDataMixin):
    def get(self, request, token):
        try:
            decoded = jwt.decode(token, settings.JWT_KEY, algorithms=[settings.JWT_ALGORITHM])
            user = AppUser.objects.get(id=decoded['user_id'])
            data = self._get_init_data(user)
            user.save()
            return Response({ "user": data['user'] }, status=status.HTTP_200_OK)
        except:
            return Response({ "message": "An error occured" }, status=status.HTTP_404_NOT_FOUND) 

class LoginView(APIView, InitDataMixin):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        
        user = get_object_or_404(AppUser, email=email)
        if user.check_password(password):
            token_data = {
                "user_id": user.id,
                "date": datetime.datetime.now().timestamp()
            }
            data = self._get_init_data(user)
            user.save()

            return Response({ 
                "token": f'{jwt.encode(token_data, settings.JWT_KEY, algorithm=settings.JWT_ALGORITHM)}',
                "user": data['user']
            }, status=status.HTTP_200_OK)
        else:
            return Response({ "detail": "User not found" }, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, token):
        try:
            decoded = jwt.decode(token, settings.JWT_KEY, algorithms=[settings.JWT_ALGORITHM])
            return Response({ "message": "Token is ok" }, status=status.HTTP_200_OK)
        except:
            return Response({ "message": "Token is wrong" }, status=status.HTTP_404_NOT_FOUND)

class SignUpView(APIView, InitDataMixin):
    def post(self, request):
        firstName = request.data["firstName"]
        lastName = request.data["lastName"]
        email = request.data["email"]
        password = request.data["password"]

        if AppUser.objects.filter(email=email).exists():
            return Response({ "detail": "User already exists" }, status=status.HTTP_401_UNAUTHORIZED)

        now = datetime.datetime.now()

        user = AppUser(
            first_name=firstName, last_name=lastName, email=email, last_logged_in_date=now
        )
        user.password = password
        user.save()

        token_data = {
            "user_id": user.id,
            "date": now.timestamp()
        }
        data = self._get_init_data(user)
        user.save()

        return Response({ 
            "token": f'{jwt.encode(token_data, settings.JWT_KEY, algorithm=settings.JWT_ALGORITHM)}',
            "user": data['user']
        }, status=status.HTTP_200_OK)