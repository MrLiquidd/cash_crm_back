from rest_framework import serializers
from accounts.api.serializers import UserModelSerializer
from leads.models import Lead
from office.api.serializer import OfficeModelSerializer


class LeadModelSerializer(serializers.ModelSerializer):
    manager = UserModelSerializer(read_only=True, label='Менеджер')
    office = OfficeModelSerializer(read_only=True)

    class Meta:
        model = Lead
        read_only_fields = (
            'created_at',
            'modified_at',
        )
        fields = '__all__'
