from rest_framework import serializers
from .models import Product, DescriptionProduct, FavoriteProducts


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DecsriptionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionProduct
        fields = "__all__"


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProducts
        fields = "__all__"
