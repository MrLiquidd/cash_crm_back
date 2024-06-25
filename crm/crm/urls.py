from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', include('swagger.urls')),
    path('api/', include('accounts.api.urls')),
    path('api/', include('leads.api.urls')),
    path('api/', include('events.api.urls')),
    path('api/', include('topics.api.urls')),
    path('api/', include('office.api.urls')),
]
