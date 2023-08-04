from rest_framework import generics
from .models import Product
from .serializer import CreateProductSerializer, ListProductSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class AddProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated]


class ListProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]
