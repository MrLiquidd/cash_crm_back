from django.urls import path, include
from rest_framework import routers
from events.api.views import EventModelViewSet

event_router = routers.DefaultRouter()
event_router.register('events', EventModelViewSet)

urlpatterns = [
    path('', include(event_router.urls)),
]
