from rest_framework import serializers
from apps.brand.models import Brand
from apps.product.models import Product


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'image_logo', 'image_circle', 'title', 'tagline', 'description', 'file',)


class AnotherProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'title',)


class AnotherProductsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Brand
        fields = ('id', 'title', 'product')

    def get_product(self, obj):
        product = obj.products.first()
        return AnotherProductSerializer(product).data if product else None
