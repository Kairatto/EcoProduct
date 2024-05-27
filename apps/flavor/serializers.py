from rest_framework import serializers
from apps.flavor.models import Flavor


class FlavorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ('id', 'image', 'title', 'description',)
