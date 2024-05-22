from rest_framework import serializers
from .models import BrandHistory, BrandInfo


class BrandHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandHistory
        fields = ('id', 'image', 'year', 'description',)


class BrandInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandInfo
        fields = ('id', 'title', 'description', 'desc_1', 'desc_2', 'desc_3', 'desc_4',)
