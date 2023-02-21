from django.shortcuts import render

# Create your views here.
from .serializers import CategorySerializer,RestaurnatSerializer
from .models import Category,Restaurnat
from rest_framework import generics,viewsets
from rest_framework_bulk import BulkModelViewSet

class RestaurnatsShow(generics.ListAPIView):
    queryset =Restaurnat.objects.all()
    serializer_class =RestaurnatSerializer

class category(BulkModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        self.queryset=Category.objects.filter(Restaurnat=self.request.user.restaurnat)
        return super().get_queryset()
