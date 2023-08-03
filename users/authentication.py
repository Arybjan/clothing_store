from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.request import Request
from django.conf import settings
import jwt

from .models import User


class JWTAuthentication(BaseAuthentication):
    prefix = "Bearer"

    def authenticate(self, request: Request):
        msg = _("Invalid basic header.")
        try:
            prefix, value = get_authorization_header(request=request).split()
        except ValueError:
            pass
        else:
            if self.prefix.lower() != prefix.decode().lower():
                raise exceptions.AuthenticationFailed(msg)
            payload = jwt.decode(value, algorithms=["HS256"],key=settings.SECRET_KEY)
            email = payload.get("email")
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed("User does not exist")
            return user, value
