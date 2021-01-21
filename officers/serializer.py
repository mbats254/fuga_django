from rest_framework import serializers
from .models import Officer


class OfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        # fields = ('name','category','price')
        fields = '__all__'


