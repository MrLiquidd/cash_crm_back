from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserModelSerializer
from accounts.models import User
from topics.models import TopicCategory


class TopicCategoryModelSerializer(serializers.ModelSerializer):
    personal_access = UserModelSerializer(read_only=True)
    author = UserModelSerializer(default=serializers.CurrentUserDefault(), read_only=True)
    reflective = UserModelSerializer(read_only=True)

    class Meta:
        model = TopicCategory
        fields = '__all__'

    def validate(self, attrs):
        reflective: User = self.context.get("request").request.user
        personal_access: User = attrs.get('personal_access')
        author: User = attrs.get('author')

        if reflective != personal_access and reflective != author:
            raise ValidationError("You can only create topics for yourself or as an author.")
