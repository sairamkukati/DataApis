"""
URL configuration for DataApis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.views import LocationViewSet, DepartmentViewSet, CategoryViewSet, SubCategoryViewSet, SKUView

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')
router.register(r'location/(?P<location_id>\d+)/department', DepartmentViewSet, basename='department')
router.register(r'location/(?P<location_id>\d+)/department/(?P<department_id>\d+)/category', CategoryViewSet, basename='category')
router.register(r'location/(?P<location_id>\d+)/department/(?P<department_id>\d+)/category/(?P<category_id>\d+)/subcategory', SubCategoryViewSet, basename='subcategory')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger-api/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-api",
    ),
    path('api/v1/', include(router.urls)),
    path('api/v1/sku/<str:location>/<str:department>/<str:category>/<str:subcategory>/', SKUView.as_view(), name = "sku"),
]