from django.urls import path, include
from rest_framework import routers

from leads.api.views import LeadsModelViewSet

lead_router = routers.DefaultRouter()
lead_router.register('leads', LeadsModelViewSet)

urlpatterns = [
    path('', include(lead_router.urls)),
]
