from rest_framework import serializers
from category.models import Category
from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner_email')

    class Meta:
        model = Product
        fields = ('id', 'owner', 'owner_email', 'price', 'image', 'stock')


class ProductSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner_email')
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'

