from django.shortcuts import render
from rest_framework import status
from rest_framework.response import response
from rest_framework.decorators import api_view

from .serializers import RegisterSerializer
# Create your views here.

@api_view(['POST',])
def reg_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors   
