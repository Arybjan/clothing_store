from rest_framework import generics, viewsets
from django.conf import settings
from .serializers import LoginSerializer, CreateUserSerializer
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
import jwt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class LoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.data.get("email"))
        except User.DoesNotExist:
            return Response(
                data={"detail": "User not found"},
                status=status.HTTP_403_FORBIDDEN,
            )

        is_password_valid = check_password(
            serializer.data.get("password"), user.password
        )
        if not is_password_valid:
            # raise ValidationError(detail="Given password is not valid")
            return Response(
                data={"detail": "Given password is not valid"},
                status=status.HTTP_403_FORBIDDEN,
            )

        token = jwt.encode(payload={"email": user.email}, key=settings.SEKRET_KEY)
        return Response
