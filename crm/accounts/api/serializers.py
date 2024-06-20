from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User


class UserModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(required=False, label='Никнейм')

    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password')
        read_only_fields = ('id', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active')


class UserModelRegistrationSerializer(UserModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs.get('password', None) != attrs.pop('password2', None):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User(email=email, username=email, **validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        exclude = ('groups', 'user_permissions',)
        read_only_fields = ('id', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active')