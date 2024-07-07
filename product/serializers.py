from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    """serializer for products"""
    class Meta:
        model= models.Product
        fields = [
            'id',
            'product_name',
            'product_price',
            'created_at',
            'product_description',
        ]
        read_only_fields = ['id', 'created_at']
