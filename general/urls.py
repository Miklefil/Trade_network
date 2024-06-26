from django.urls import path, include
from rest_framework.routers import DefaultRouter

from general.apps import GeneralConfig
from general.views import ProviderViewSet, NetworkViewSet, ProductViewSet

app_name = GeneralConfig.name

router = DefaultRouter()
router.register(r'provider', ProviderViewSet, basename='provider')

router_network = DefaultRouter()
router_network.register(r'network', NetworkViewSet, basename='network')

router_product = DefaultRouter()
router_product.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_network.urls)),
    path('', include(router_product.urls)),
]
