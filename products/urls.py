from rest_framework.routers import DefaultRouter
from products import views
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path("add-product/", views.AddProductAPIView.as_view(), name="add-product"),
    path("list-product/", views.ListProductAPIView.as_view(), name="list-product"),
    path(
        "add-description/",
        views.DecsriptionProductAPIView.as_view(),
        name="add-description",
    ),
]
