from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from events.api.serializers import EventModelSerializer
from events.models import Event


class EventModelViewSet(viewsets.ModelViewSet):
    serializer_class = EventModelSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ('is_active', )
    queryset = Event.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(reflective=user)
        return qs


class EventRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EventModelSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'
    queryset = Event.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(client__manager=user)
        return qs
