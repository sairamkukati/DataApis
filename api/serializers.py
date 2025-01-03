from rest_framework import serializers
from .models import Location, Department, Category, SubCategory, SKU


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    location = LocationSerializer() 
    class Meta:
        model = Department
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer() 
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer() 
    class Meta:
        model = SubCategory
        fields = "__all__"


class SKUSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer() 

    class Meta:
        model = SKU
        fields = "__all__"
