from django.urls import path, include
from rest_framework import routers
from office.api.views import OfficeModelViewSet

office_router = routers.DefaultRouter()
office_router.register('office', OfficeModelViewSet)

urlpatterns = [
    path('', include(office_router.urls)),
]
