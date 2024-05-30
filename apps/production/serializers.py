from rest_framework import serializers
from .models import ProductionShort


class ProductionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionShort
        fields = ('id', 'image', 'title', 'description', 'language',)
