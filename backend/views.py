from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def get(self, request):
        print("=> Hello world")
        return Response({ "message": "Token OK" }, status=status.HTTP_200_OK)