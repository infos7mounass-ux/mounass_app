from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextItemViewSet

router = DefaultRouter()
router.register(r'texts', TextItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
