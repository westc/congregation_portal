from rest_framework import routers
from api import views

router = routers.DefaultRouter()

# shared api routers
router.register(r'congregation', views.CongregationViewSet)

# territory api routers
router.register(r'territory', views.TerritoryViewSet)
router.register(r'territory/(?P<territory_id>\d+)/item', views.TerritoryItemViewSet)