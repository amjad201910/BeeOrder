from .models import Meal
from rest_framework import serializers
from restaurant.models import Category
from rest_framework.reverse import reverse
from django.db.models import Q

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)


class MealSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    #url=serializers.SerializerMethodField(read_only=True)
    Type= serializers.CharField(source='Type.Name')
    class Meta:
        model = Meal
        list_serializer_class = BulkListSerializer
        fields = ['Name','Image','Body','Type','Price','url']
    def create(self, validated_data):

         validated_data['Type']=Category.objects.filter(Q(Restaurnat= self.context['request'].user.restaurnat)&Q(Name=validated_data['Type']['Name'])).first()

         validated_data['Restaurnat']= self.context['request'].user.restaurnat
         return super().create(validated_data)
    def update(self, instance, validated_data):
        validated_data['Type'] = Category.objects.filter(
            Q(Restaurnat=self.context['request'].user.restaurnat) & Q(Name=validated_data['Type']['Name'])).first()
        return super().update(instance, validated_data)




class MealShowSerializer(serializers.ModelSerializer):
    Type= serializers.CharField(source='Type.Name',read_only=True)
    class Meta:
        model = Meal
        fields = ['Name','Image','Body','Type','Price']