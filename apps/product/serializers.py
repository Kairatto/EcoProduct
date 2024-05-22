from rest_framework import serializers
from .models import Product, Volume


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'volume', 'brand', 'flavor',)


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('id', 'title',)
