from rest_framework.routers import DefaultRouter
from django.urls import path
from users import views


router = DefaultRouter()
router.register("users", views.UserViewSet)
urlpatterns = [
    path("api-auth", views.LoginAPIView.as_view()),
] + router.urls
