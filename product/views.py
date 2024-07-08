from rest_framework import viewsets, status, generics, mixins
from . import serializers, models

class ManageProducts(viewsets.ModelViewSet):
    """Perform CRUD on Products"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    