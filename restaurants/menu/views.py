from django.shortcuts import render

# Create your views here.

from .models import Meal
from rest_framework import generics,viewsets
from rest_framework_bulk import BulkModelViewSet
from .serializers import MealSerializer,MealShowSerializer



class meal(BulkModelViewSet):
    serializer_class = MealSerializer

    def get_queryset(self):
        self.queryset=Meal.objects.filter(Restaurnat=self.request.user.restaurnat)
        return super().get_queryset()

class mealShow(generics.ListAPIView):
    serializer_class = MealShowSerializer

    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset=Meal.objects.filter(Restaurnat=pk)
        return super().get_queryset()
