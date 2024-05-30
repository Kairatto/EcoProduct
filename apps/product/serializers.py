from rest_framework import serializers

from apps.brand.models import Brand
from apps.flavor.models import Flavor
from apps.language.serializers import LanguageSerializer
from apps.product.models import Product, Category


def get_full_url(request, path):
    if request:
        return request.build_absolute_uri(path)
    return path


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    image = serializers.SerializerMethodField()
    language = LanguageSerializer()

    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'brand', 'language', 'flavor', 'category',)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return get_full_url(request, obj.image.url)
        return None


class FlavorSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    language = LanguageSerializer()

    class Meta:
        model = Flavor
        fields = ['id', 'title', 'image', 'description', 'language', 'products']

    def get_products(self, obj):
        products = Product.objects.filter(flavor=obj)
        return ProductSerializer(products, many=True, context=self.context).data

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return get_full_url(request, obj.image.url)
        return None


class BrandSerializer(serializers.ModelSerializer):
    flavors = serializers.SerializerMethodField()
    image_logo = serializers.SerializerMethodField()
    image_circle = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()
    language = LanguageSerializer()

    class Meta:
        model = Brand
        fields = ['id', 'image_logo', 'image_circle', 'background', 'title',
                  'tagline', 'description', 'file', 'language', 'flavors']

    def get_flavors(self, obj):
        flavors = Flavor.objects.filter(products__brand=obj).distinct()
        return FlavorSerializer(flavors, many=True, context=self.context).data

    def get_image_logo(self, obj):
        request = self.context.get('request')
        if obj.image_logo:
            return get_full_url(request, obj.image_logo.url)
        return None

    def get_image_circle(self, obj):
        request = self.context.get('request')
        if obj.image_circle:
            return get_full_url(request, obj.image_circle.url)
        return None

    def get_background(self, obj):
        request = self.context.get('request')
        if obj.background:
            return get_full_url(request, obj.background.url)
        return None
