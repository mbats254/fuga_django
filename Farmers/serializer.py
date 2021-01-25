from rest_framework import serializers
from .models import  Farmers, Visits, Farm

class FarmersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmers
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'