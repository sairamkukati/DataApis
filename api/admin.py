from django.contrib import admin
from .models import Location, Department, Category, SubCategory, SKU

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location")
    search_fields = ("name", "location__name")
    list_filter = ("location",)
    ordering = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "department")
    search_fields = ("name", "department__name")
    list_filter = ("department",)
    ordering = ("name",)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    ordering = ("name",)

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = ("id", "sku", "description")
    search_fields = ("sku", "description")
    ordering = ("sku",)


