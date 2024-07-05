from rest_framework import serializers
from apps.brand.models import Brand
from apps.product.models import Product


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'image_logo', 'image_circle', 'image_main', 'background', 'flavor_bg',
                  'title', 'tagline', 'description', 'file', 'language',)
