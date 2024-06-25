import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from events.api.serializers import EventModelSerializer, EventCommentSerializer
from events.models import Event, EventComment


class EventModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventModelSerializer
    queryset = Event.objects.all().prefetch_related('event_comment__author')
    filterset_fields = ('is_active',)

    def get_queryset(self):
        qs = self.queryset
        print(qs)
        if not self.request.user.is_superuser:
            qs = qs.filter(reflective=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(
            reflective=self.request.user,
            creator_id=self.request.data.get('creator', None),
            client_id=self.request.data.get('client', None),
            office_id=self.request.data.get('office', None)
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        reflective_id = self.request.data.get('reflective', None)
        reflective = get_object_or_404(User, id=reflective_id) if reflective_id else self.request.user

        serializer.save(
            reflective=reflective,
            client_id=self.request.data.get('client', None)['id'],
            office_id=self.request.data.get('office', None)['id']
        )


class ActiveEventModelViewSetClient(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventModelSerializer
    queryset = Event.objects.all().prefetch_related('event_comment__author')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']  # добавлено поле client в filterset_fields

    def get_queryset(self):
        qs = self.queryset
        client_id = self.kwargs.get('client')
        if client_id is not None:
            qs = qs.filter(client_id=client_id, is_active=True)
        return qs


class UnActiveEventModelViewSetClient(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']  # добавлено поле client в filterset_fields

    def get_queryset(self):
        qs = self.queryset
        client_id = self.kwargs.get('client')
        if client_id is not None:
            qs = qs.filter(client_id=client_id, is_active=False)
        return qs


class EventRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EventModelSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    queryset = Event.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset
        if not self.request.user.is_superuser:
            qs = qs.filter(client__manager=user)
        return qs


class EventCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventCommentSerializer
    queryset = EventComment.objects.all()

    def perform_create(self, serializer):
        print(self.request.data)
        event_id = self.request.data.get('event', None)
        serializer.save(author_id=self.request.user.id, event_id=event_id)
