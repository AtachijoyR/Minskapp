from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pet
        fields =('__all__') 

class PetSerializerWithDescription(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    breed = serializers.CharField()
    age_months = serializers.IntegerField()
    weight = serializers.IntegerField()
    status = serializers.CharField()
    specie = serializers.CharField()
    rut_owner = serializers.CharField()
