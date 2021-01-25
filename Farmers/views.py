from django.shortcuts import render,get_object_or_404
from .models import  Farmers, Visits, Farm
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import  FarmersSerializer, VisitSerializer, FarmSerializer
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import viewsets
from rest_framework.response import Response



class FarmersViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Farmers.objects.all()
    serializer_class = FarmersSerializer
    # def list(self, request):
    #     queryset = Farmers.objects.all()
    #     serializer = FarmersSerializer(queryset, )
    #     return Response(serializer.data)

class VisitViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Visits.objects.all()
    serializer_class = VisitSerializer

class FarmViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
   
        

# Create your views here.
class FarmersLists(APIView):
    def get(self, request):
        farmers = Farmers.objects.all()
        serializer = FarmersSerializer(farmers, many= True)
        return Response(serializer.data)

def delete_it(request):     
        Visits.objects.filter(id=2).delete()
       
