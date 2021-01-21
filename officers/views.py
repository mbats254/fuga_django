from django.shortcuts import render,get_object_or_404
from .models import Officer
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OfficersSerializer
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from .forms import RegisterOfficer
# Create your views here.
def officer_list(request):
    context = {
        "officers": Officer.objects.all()
    }
    return render(request,"officers/officer_list.html", context)

def single_officer(request, officer_id):
     try:
         officer = Officer.objects.get(pk=officer_id)
     except Officer.DoesNotExist:
         raise Http404("Officer does not exists.") 
     context = {
          "officer": officer,
 
      }   
     return render(request,"officers/single_officer.html", context)

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request,'registraton/register.html',context)

def index(request):
    return render(request,'officers/index.html')    

def deactivate_officer(request):     
         officer = Officer.objects.get(pk=officer_id)
         officer.status = 1
         officer.save() 
  

class RegisterOfficers(TemplateView):
    template = 'officers/register_officer.html'
    def get(self, request):
        form  = RegisterOfficer()
        return render(request, self.template,{'form': form}) 
    

    def post(self, request):
        form = UserCreationForm(request.POST)        
        if form.is_valid():
            user_name = form.cleaned_data['name']            
            user_email = form.cleaned_data['email']
            officer_county = form.cleaned_data['county']
            officer_id_no  = form.cleaned_data['id_no']
            officer_phone_no = form.cleaned_data['phone_no']
        args = {'form':form, 'user_name': user_name, 
        #'email': user_email, 'county': officer_county, 'id_no': officer_id_no, 'phone_number' : officer_phone_number 
        }
        return name
        # return render(request, self.template, args)

class OfficersList(APIView):
    def get(self, request):
        officers = Officer.objects.all()
        serializer = OfficersSerializer(officers, many= True)
        return Response(serializer.data)  



        
     
      
   