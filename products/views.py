from rest_framework import generics
from .models import Product, DescriptionProduct
from .serializer import (
    CreateProductSerializer,
    ListProductSerializer,
    DecsriptionProductSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny


class AddProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated]


class ListProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]


class DecsriptionProductAPIView(generics.CreateAPIView):
    queryset = DescriptionProduct.objects.all()
    serializer_class = DecsriptionProductSerializer
    permission_classes = [IsAuthenticated]
