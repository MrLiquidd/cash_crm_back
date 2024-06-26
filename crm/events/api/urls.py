from django.urls import path, include
from rest_framework import routers
from events.api.views import EventModelViewSet, ActiveEventModelViewSetClient, UnActiveEventModelViewSetClient, \
    EventCommentViewSet

event_router = routers.DefaultRouter()
event_router.register('events', EventModelViewSet)
event_router.register(r'event-comments', EventCommentViewSet)

urlpatterns = [
    path('', include(event_router.urls)),
    path('events/client/active/<int:client>/', ActiveEventModelViewSetClient.as_view({'get': 'list'}), name='event-list-client'),
    path('events/client/unactive/<int:client>/', UnActiveEventModelViewSetClient.as_view({'get': 'list'}), name='event-list-client'),
]
