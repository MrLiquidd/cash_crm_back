from rest_framework import serializers
from .models import Lead, User, UserInfo, Event, TopicCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class UserInfoSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user.email")
    avatar = serializers.ReadOnlyField(source="user.avatar")

    class Meta:
        model = UserInfo
        fields = ['id', 'user', 'email', 'job_title', 'avatar', 'name', 'surname', 'last_name', 'office', 'phone', 'username',
                  'term_work', 'passport', 'hire_data']


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'


class LeadDetailSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField()

    class Meta:
        model = Lead
        fields = (
            'id', 'name', 'office', 'email', 'phone', 'status', 'manager', 'manager_name', 'created_at', 'modified_at')

    def get_manager_name(self, obj):
        return f"{obj.manager.first_name} {obj.manager.last_name}"


class LeadSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)

    class Meta:
        model = Lead
        read_only_fields = (
            'created_at',
            'modified_at',
        )
        fields = [
            'id',
            'name',
            'office',
            'email',
            'phone',
            'status',
            'manager',
        ]


class LeadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'name', 'office']


class EventSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    office = serializers.CharField(source='client.office', read_only=True)
    reflective = serializers.CharField(source='reflective.email', read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class TopicCategorySerializer(serializers.ModelSerializer):
    reflective_full_name = serializers.SerializerMethodField()
    personal_access_full_name = serializers.SerializerMethodField()
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = TopicCategory
        fields = [
            'id', 'theme', 'status', 'reflective', 'reflective_full_name',
            'personal_access', 'personal_access_full_name', 'open_topic',
            'deadline', 'author', 'author_full_name'
        ]

    def get_reflective_full_name(self, obj):
        return self.get_full_name(obj.reflective)

    def get_personal_access_full_name(self, obj):
        return self.get_full_name(obj.personal_access)

    def get_author_full_name(self, obj):
        return self.get_full_name(obj.author)

    def get_full_name(self, user):
        try:
            user_info = UserInfo.objects.get(user=user)
            return user_info.full_name()
        except UserInfo.DoesNotExist:
            return f"{user.username} (UserInfo not found)"
