from rest_framework import serializers
from ..models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField()

    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']