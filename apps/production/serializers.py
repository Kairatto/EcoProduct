from rest_framework import serializers
from .models import ProductionShort, ProductionProcess, Production, ProductionPath


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ('id', 'image', 'title', 'description', 'language',)


class ProductionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionShort
        fields = ('id', 'image', 'title', 'description', 'language',)


class ProductionProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionProcess
        fields = ('id', 'title', 'text_1', 'text_2', 'text_3', 'text_4', 'fact_title', 'fact_text', 'language',)


class ProductionPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPath
        fields = ('id', 'title', 'title_1', 'desc_1', 'image_1', 'title_2', 'desc_2', 'image_2',
                  'title_2', 'desc_2', 'image_2', 'title_3', 'desc_3', 'image_3',
                  'title_4', 'desc_4', 'image_4', 'title_4', 'desc_4', 'image_4',
                  'title_5', 'desc_5', 'image_5', 'title_6', 'desc_6', 'image_6', 'language',)
