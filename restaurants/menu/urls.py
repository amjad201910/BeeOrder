
from django.urls import path, include
from rest_framework import routers
from .views import meal,mealShow

router = routers.DefaultRouter()
router.register(r'meal', meal, basename="meal")

urlpatterns = [
    path('<int:pk>/', mealShow.as_view(), name="show-meal"),

    path('', include(router.urls)),

]
