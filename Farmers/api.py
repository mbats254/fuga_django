from .models import Farmers
from rest_framework import viewsets, permissions
from .serializer import FarmersSerializer

#View Set
class FarmersViewSet(viewsets.ModelViewSet):
    queryset = Farmers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FarmersSerializer
    # serializer_class.save()