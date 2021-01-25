from rest_framework import routers
from Farmers.views import FarmersViewSet, VisitViewSet, FarmViewSet
from rest_framework import renderers

router = routers.DefaultRouter()
router.register('farmers',FarmersViewSet)
router.register('visits',VisitViewSet)
router.register('farms',FarmViewSet)



# for url in router.urls:
#     print(url, '\n')