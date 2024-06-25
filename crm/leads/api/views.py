from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
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
        manager_id = self.request.data.get('manager', None)
        office_id = self.request.data.get('office', None)
        if manager_id:
            serializer.save(manager_id=manager_id, office_id=office_id)
        else:
            # Или автоматически назначаем текущего пользователя в качестве менеджера
            serializer.save(manager=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        manager_id = self.request.data.get('manager', None)

        serializer.save(
            manager_id=manager_id,
            office_id=self.request.data.get('office', None)
        )
