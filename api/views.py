from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location, Department, Category, SubCategory, SKU
from .serializers import LocationSerializer,DepartmentSerializer, CategorySerializer, SubCategorySerializer, SKUSerializer

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Department.objects.filter(location_id=location_id)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        department_id = self.kwargs['department_id']
        return Category.objects.filter(department__location_id=location_id, department_id=department_id)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        department_id = self.kwargs['department_id']
        category_id = self.kwargs['category_id']
        return SubCategory.objects.filter(category__department__location_id=location_id, category__department_id=department_id, category_id=category_id)


class SKUView(APIView):

    def get(self, request, *args, **kwargs):
        location = self.kwargs['location']
        department = self.kwargs['department']
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        skus = SKU.objects.all()
        if location:
            skus = skus.filter(subcategory__category__department__location__name__iexact=location)
        if department:
            skus = skus.filter(subcategory__category__department__name__iexact=department)
        if category:
            skus = skus.filter(subcategory__category__name__iexact=category)
        if subcategory:
            skus = skus.filter(Q(subcategory__name__icontains=subcategory) | Q(subcategory__name__istartswith=subcategory))
        serializers = SKUSerializer(skus, many=True)
        return Response(serializers.data)