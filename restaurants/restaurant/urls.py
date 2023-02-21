from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import category,RestaurnatsShow

router = routers.DefaultRouter()
router.register(r'category', category, basename="category")
urlpatterns = [
    path('', RestaurnatsShow.as_view(), name="show"),
    path('menu/', include('menu.urls')),
    path('', include(router.urls)),
]
