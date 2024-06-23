from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from events.api.serializers import EventModelSerializer
from events.models import Event


class EventModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    filterset_fields = ('is_active', )

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(reflective=self.request.user)
        return qs

    def perform_create(self, serializer):
        reflective = self.request.data.get('reflective', None)
        if reflective:
            serializer.save(reflective=reflective)
        else:
            serializer.save(manager=self.request.user)


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
