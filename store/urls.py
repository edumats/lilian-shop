from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store import views

router = DefaultRouter()
router.register(r'hantems', views.HantemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
