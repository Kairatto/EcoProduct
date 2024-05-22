from rest_framework import serializers
from .models import Production, ProductionShort


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ('id', 'image', 'title', 'description',)


class ProductionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionShort
        fields = ('id', 'image', 'title', 'description',)
