from django.shortcuts import render,get_object_or_404
from .models import  Farmers
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import  FarmersSerializer
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView


# Create your views here.
class FarmersLists(APIView):
    def get(self, request):
        farmers = Farmers.objects.all()
        serializer = FarmersSerializer(farmers, many= True)
        return Response(serializer.data)