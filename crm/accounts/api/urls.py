from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from accounts.api.views import UserModelViewSet

accounts = routers.DefaultRouter()
accounts.register(r'accounts', UserModelViewSet)

urlpatterns = [
    path('', include(accounts.urls)),
    path('accounts/login', TokenObtainPairView.as_view(), name='token_obtain'),
    path('accounts/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/verify', TokenVerifyView.as_view(), name='token_verify'),
]
