from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from leads.api.serializers import LeadModelSerializer
from leads.models import Lead


class LeadsModelViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = LeadModelSerializer
    queryset = Lead.objects.all()
    filterset_fields = ('is_active', )

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(manager=self.request.user)
        return qs

    def perform_create(self, serializer):
        # Получаем переданного менеджера, если он указан
        manager_id = self.request.data.get('manager', None)
        if manager_id:
            serializer.save(manager_id=manager_id)
        else:
            # Или автоматически назначаем текущего пользователя в качестве менеджера
            serializer.save(manager=self.request.user)
