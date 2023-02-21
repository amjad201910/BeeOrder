from .models import Category,Restaurnat
from rest_framework import serializers

from rest_framework.reverse import reverse


from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)



class RestaurnatSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='show-meal',lookup_field='pk',read_only=True)

    class Meta:
        model = Restaurnat

        fields = ['Name','Image','Address','url']

class CategorySerializer(BulkSerializerMixin,serializers.ModelSerializer):
    #url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        list_serializer_class = BulkListSerializer
        fields = ['Name','url']
    def create(self, validated_data):
         validated_data['Restaurnat']= self.context['request'].user.restaurnat
         return super().create(validated_data)





    """  def get_url1(self, obj):
        request = self.context.get('request')
        if obj.Name=="n":
            return None
        else:
            return reverse('category-detail', args=[str(obj.pk)],request=request)
           """