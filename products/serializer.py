from rest_framework import serializers
from .models import Product


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
