from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from leads.api.serializers import LeadModelSerializer
from leads.models import Lead


class LeadsModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = LeadModelSerializer
    queryset = Lead.objects.all()
    filterset_fields = ('is_active', )

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(manager=self.request.user)
        return qs