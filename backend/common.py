from users.models import AppUser
from rest_framework.permissions import BasePermission
import jwt
from django.conf import settings

class IsAuthenticate(BasePermission):
    def has_permission(self, request, view):
        token = view.kwargs.get('token', None)
        is_allowed = False
        try:
            if token:
                decoded_token = jwt.decode(token, settings.JWT_KEY, algorithms=[settings.JWT_ALGORITHM])
                user = AppUser.objects.filter(id=decoded_token['user_id'])
                is_allowed = user.exists()

                if is_allowed:
                    request.user = user.first()
        except:
            pass

        return is_allowed