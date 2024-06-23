from django_filters.rest_framework import DjangoFilterBackend
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
        client = self.request.data.get('client', None)
        if reflective:
            serializer.save(reflective_id=reflective, client_id=client)
        else:
            serializer.save(reflective=self.request.user, client_id=client)

class ActiveEventModelViewSetClient(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']  # добавлено поле client в filterset_fields

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_superuser:
            client_id = self.request.query_params.get('client')  # получаем id клиента из параметров запроса
            if client_id is not None:
                qs = qs.filter(client_id=client_id, is_active=False)
            else:
                qs = qs.none()  # если id клиента не указан, возвращаем пустой queryset
        return qs

class UnActiveEventModelViewSetClient(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_superuser:
            client_id = self.request.query_params.get('client')
            if client_id is not None:
                qs = qs.filter(client_id=client_id, is_active=False)
            else:
                qs = qs.none()
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
