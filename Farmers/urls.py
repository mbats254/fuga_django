from django.urls import path, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .api import FarmersViewSet




urlpatterns = [
 path(r'list', views.FarmersLists.as_view(), name='farmers.list'), 
    path(r"delete/it", views.delete_it, name="delete_it"),
#  path(r'api/', include('router'), name='farmers.list'), 
   
]
