from django.urls import path, include
from rest_framework import routers
from .views import PieceViewSet, BoardViewSet

router = routers.DefaultRouter()
router.register('pieces', PieceViewSet)
router.register('boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
