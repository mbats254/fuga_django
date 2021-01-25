from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .api import FarmersViewSet


router = routers.DefaultRouter()
router.register('farmer/',FarmersViewSet, base_name='farmers')
router.register('visit/',FarmersViewSet, base_name='visit')