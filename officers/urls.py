from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r"officer/list", views.officer_list, name="officer_list"),
    path(r"single/officer/<int:officer_id>", views.single_officer, name="single_officer"),

    path(r'all/officers/api/', views.OfficersList.as_view()),
    path(r'register/', views.register, name='register'),
    path(r'register/officer', views.RegisterOfficers.as_view(), name='register.officer'),
    path(r'deactivate/officer/<int:officer_id>', views.deactivate_officer, name='deactivate.officer'),
    
    
   
    
    
]