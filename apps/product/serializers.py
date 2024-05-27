from rest_framework import serializers

from apps.brand.models import Brand
from apps.flavor.models import Flavor
from apps.product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'category', 'brand', 'flavor',)


class FlavorSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Flavor
        fields = ['id', 'title', 'image', 'description', 'products']

    def get_products(self, obj):
        products = Product.objects.filter(flavor=obj)
        return ProductSerializer(products, many=True).data


class BrandSerializer(serializers.ModelSerializer):
    flavors = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ['id', 'image_logo', 'image_circle', 'title', 'tagline', 'description', 'file', 'flavors']

    def get_flavors(self, obj):
        flavors = Flavor.objects.filter(products__brand=obj).distinct()
        return FlavorSerializer(flavors, many=True).data
