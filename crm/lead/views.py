from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .models import Lead, Event, TopicCategory, UserInfo
from .serializers import LeadSerializer, EventSerializer, TopicCategorySerializer, UserInfoSerializer


class UserInfoDetail(APIView):
    def get(self, request, user_id):
        try:
            user_info = UserInfo.objects.get(user_id=user_id)
            serializer = UserInfoSerializer(user_info)
            return JsonResponse(serializer.data)
        except UserInfo.DoesNotExist:
            return Response({'error': 'UserInfo not found'}, status=404)


class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]


class UserLeadsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        leads = Lead.objects.filter(manager=user)
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)


class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(reflective=user)

    def perform_create(self, serializer):
        user = self.request.user
        lead_ids = Lead.objects.filter(manager=user).values_list('id', flat=True)
        if serializer.validated_data['client'].id in lead_ids:
            serializer.save()
        else:
            raise serializers.ValidationError("Вы не можете создать событие для этого клиента.")


class EventRetrieveView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(client__manager=user)


class TopicCategoryListCreateView(generics.ListCreateAPIView):
    queryset = TopicCategory.objects.all()
    serializer_class = TopicCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        reflective = self.request.user
        personal_access = serializer.validated_data.get('personal_access')
        author = serializer.validated_data.get('author')

        if reflective != personal_access and reflective != author:
            raise ValidationError("You can only create topics for yourself or as an author.")

        serializer.save(reflective=reflective)

    def get_queryset(self):
        user = self.request.user
        return TopicCategory.objects.filter(personal_access=user)


class ActiveEventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        client_id = self.request.query_params.get('client')
        print(client_id)
        return Event.objects.filter(client_id=client_id, is_active=True)


class InactiveEventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        client_id = self.request.query_params.get('client')
        print(client_id)
        return Event.objects.filter(client_id=client_id, is_active=False)
