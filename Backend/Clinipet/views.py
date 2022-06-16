from django.shortcuts import render

from .models import Pet
from rest_framework.generics import ListAPIView
from rest_framework import status

from .serializers import PetSerializer
# Create your views here.



class ListPets(ListAPIView):
    serializer_class = PetSerializer
    def get_queryset(self):
        return Pet.objects.all()




