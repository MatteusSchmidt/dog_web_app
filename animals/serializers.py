from rest_framework import serializers
from .models import CatModel, DogModel


# serializers for each data model, to be called as an api in order to create the sort by functions
class CatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatModel
        fields = '__all__'


class DogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogModel
        fields = '__all__'
