from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api
from .views import UserLeadsView, EventListCreateView, EventRetrieveView, TopicCategoryListCreateView, LeadDetailView, \
    UserInfoDetail, ActiveEventListView, InactiveEventListView

urlpatterns = [
    path('account/', api.me, name='account'),
    path('user/<uuid:user_id>/', UserInfoDetail.as_view(), name='user-detail'),

    path('leads/', UserLeadsView.as_view(), name='user-leads'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),

    path('events/active/', ActiveEventListView.as_view(), name='active-event-list'),
    path('events/inactive/', InactiveEventListView.as_view(), name='inactive-event-list'),

    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:id>/', EventRetrieveView.as_view(), name='event-retrieve'),

    path('topic-categories/', TopicCategoryListCreateView.as_view(), name='topiccategory-list-create'),

    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]
