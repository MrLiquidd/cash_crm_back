from django.urls import path
from leads.api.views import UserLeadsView, LeadDetailView

urlpatterns = [
    path('leads/', UserLeadsView.as_view(), name='user-leads'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='leads-detail'),
]
