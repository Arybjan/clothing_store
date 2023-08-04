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
    path(
        "add-favorite-list/",
        views.FavoriteProductAPIView.as_view(),
        name="add-favorite-list",
    ),
    path(
        "update-list-favorite-product/<int:pk>/",
        views.UpdateFavoriteProductAPIView.as_view(),
        name="update-list-favorite-product",
    ),
    path(
        "list-favorite-product/",
        views.ListFavoriteProductAPIView.as_view(),
        name="list-favorite-product",
    ),
]
