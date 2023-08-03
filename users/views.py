from rest_framework import generics
from django.conf import settings
from .serializers import LoginSerializer, CreateUserSerializer, ListUserSerializer
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
import jwt


class ListUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [IsAuthenticated]


class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class LoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

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

        token = jwt.encode(payload={"email": user.email}, key=settings.SECRET_KEY)
        return Response(data={"token": token})
