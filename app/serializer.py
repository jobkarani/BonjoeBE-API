from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug','image', 'products']

class PhoneSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Phones
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

class PhoneCategorySerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    class Meta:
        model = PhoneCategory
        fields = ['id', 'name', 'slug', 'phones']

class FridgeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Fridge
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

class FridgeCategorySerializer(serializers.ModelSerializer):
    fridges = FridgeSerializer(many=True, read_only=True)
    class Meta:
        model = FridgeCategory
        fields = ['id', 'name', 'slug', 'fridges']

class HomeAppliancesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = HomeAppliances
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

class HomeAppliancesCategorySerializer(serializers.ModelSerializer):
    homeAppliances = HomeAppliancesSerializer(many=True, read_only=True)
    class Meta:
        model = HomeAppliancesCategory
        fields = ['id', 'name', 'slug', 'homeAppliances']
