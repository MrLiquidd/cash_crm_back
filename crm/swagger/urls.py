from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', SpectacularAPIView.as_view(), name='schema'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
