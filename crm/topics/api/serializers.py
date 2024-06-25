from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserModelSerializer
from accounts.models import User
from office.api.serializer import OfficeModelSerializer
from topics.models import Topic


class TopicModelSerializer(serializers.ModelSerializer):
    personal_access = UserModelSerializer(read_only=True)
    author = UserModelSerializer(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
