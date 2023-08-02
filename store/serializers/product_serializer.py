from decimal import Decimal
from rest_framework import serializers
from ..models import Product, Collection
from .collection_serializer import CollectionSerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    # Custom serializer field
    price_with_tax = serializers.SerializerMethodField('calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all()) # To send collection foreign key
    # collection = serializers.StringRelatedField() # To send collection as string representation
    collection = CollectionSerializer() # To send nested object

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
