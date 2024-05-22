from rest_framework import serializers
from .models import Video, LogoCompany


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'video', 'title')


class LogoCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoCompany
        fields = ('id', 'image', 'title')
