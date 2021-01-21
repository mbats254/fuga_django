from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/officer/list", views.officer_list, name="officer_list"),
    path("single/officer/<int:officer_id>", views.single_officer, name="single_officer"),

    path('all/officers/api/', views.OfficersList.as_view()),
    path('register/', views.register, name='register'),
    path('register/officer', views.RegisterOfficers.as_view(), name='register.officer'),
    path('deactivate/officer/<int:officer_id>', views.deactivate_officer, name='deactivate.officer'),
    
   
    
    
]