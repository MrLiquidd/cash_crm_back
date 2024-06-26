from rest_framework import serializers

from office.models import Office


class OfficeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'
