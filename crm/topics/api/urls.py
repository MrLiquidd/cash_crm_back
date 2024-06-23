from django.urls import path, include
from rest_framework import routers

from topics.api.views import TopicCategoryModelViewSet

topic_router = routers.DefaultRouter()
topic_router.register('topics', TopicCategoryModelViewSet)

urlpatterns = [
    path('', include(topic_router.urls)),
]
