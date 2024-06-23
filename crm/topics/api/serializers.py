from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserModelSerializer
from accounts.models import User
from topics.models import TopicCategory


class TopicCategoryModelSerializer(serializers.ModelSerializer):
    personal_access = UserModelSerializer(read_only=True)
    author = UserModelSerializer(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = TopicCategory
        fields = '__all__'
