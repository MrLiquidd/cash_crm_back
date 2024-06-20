from rest_framework import serializers

from accounts.api.serializers import UserModelSerializer
from leads.models import Lead


class LeadModelSerializer(serializers.ModelSerializer):
    manager = UserModelSerializer(read_only=True, label='Менеджер')

    class Meta:
        model = Lead
        read_only_fields = (
            'created_at',
            'modified_at',
        )
        fields = '__all__'

    @staticmethod
    def get_manager_name(obj) -> str:
        return f"{obj.manager.first_name} {obj.manager.last_name}"


class LeadUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'office', )
