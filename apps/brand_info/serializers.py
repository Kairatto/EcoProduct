from rest_framework import serializers
from .models import BrandHistory, BrandInfo


class BrandHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandHistory
        fields = ('id', 'image', 'year', 'description', 'language',)


class BrandInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandInfo
        fields = ('id', 'title', 'description', 'title_1', 'desc_1', 'title_2', 'desc_2', 'title_3', 'desc_3', 'title_4', 'desc_4', 'language',)
