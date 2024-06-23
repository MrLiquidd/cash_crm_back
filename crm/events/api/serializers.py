from rest_framework import serializers

from accounts.api.serializers import UserModelSerializer
from events.models import Event
from leads.models import Lead


class EventModelSerializer(serializers.ModelSerializer):
    client = UserModelSerializer(read_only=True)
    reflective = UserModelSerializer(read_only=True)

    # def validate(self, attrs):
    #     user = self.context.get("request").user
    #     lead_ids = Lead.objects.filter(manager=user).values_list('id', flat=True)
    #     client = attrs.validated_data.get('client')
    #     if not (client and client.id in lead_ids):
    #         raise serializers.ValidationError("Вы не можете создать событие для этого клиента.")
    #     return attrs

    class Meta:
        model = Event
        fields = '__all__'
