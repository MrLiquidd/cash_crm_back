import json

from rest_framework import serializers

from accounts.api.serializers import UserModelSerializer
from events.models import Event, EventComment
from office.api.serializer import OfficeModelSerializer


class EventModelSerializer(serializers.ModelSerializer):
    client = UserModelSerializer(read_only=True)
    reflective = UserModelSerializer(read_only=True)
    office = OfficeModelSerializer(read_only=True)
    creator = UserModelSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    comments_main = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    @staticmethod
    def get_comments(obj):
        comments = EventComment.objects.filter(event=obj.id)
        return [comment.comment for comment in comments]

    @staticmethod
    def get_comments_main(obj):
        comments = EventComment.objects.filter(event=obj.id)
        return [str(comment.author) + ' ' + str(comment.date) for comment in comments]


class EventCommentSerializer(serializers.ModelSerializer):
    author = UserModelSerializer(read_only=True)
    event = EventModelSerializer(read_only=True)

    class Meta:
        model = EventComment
        fields = '__all__'
