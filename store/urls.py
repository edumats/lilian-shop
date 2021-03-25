from django.urls import path
from .views import HantemDetailView, HantemListView

urlpatterns = [
    path('product/<slug:slug>', HantemDetailView.as_view(), name='product-detail'),
    path('products/', HantemListView.as_view(), name='hantem-list'),
]
