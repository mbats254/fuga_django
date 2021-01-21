from django.urls import path

from . import views

urlpatterns = [
 path('list', views.FarmersLists.as_view(), name='farmers.list'), 
   
]
