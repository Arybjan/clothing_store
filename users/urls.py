from rest_framework.routers import DefaultRouter
from django.urls import path
from users import views


router = DefaultRouter()
urlpatterns = [
    path("obtain-token/", views.LoginAPIView.as_view(), name="obtain-token"),
    path("register/", views.RegisterViewSet.as_view(), name="register"),
    path("list-users/", views.ListUsersAPIView.as_view(), name="list-user"),
]
