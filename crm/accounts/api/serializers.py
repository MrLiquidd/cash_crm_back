from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User


USER_READ_ONLY_FIELDS = ('id', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active')


class UserModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())],
        label='Электронная почта'
    )
    username = serializers.CharField(required=False, label='Никнейм')
    last_name = serializers.CharField(write_only=True, required=False, label='Отчество')
    first_name = serializers.CharField(write_only=True, required=False, label='Имя')
    surname = serializers.CharField(write_only=True, required=False, label='Фамилия')
    full_name = serializers.SerializerMethodField(label='ФИО')

    @staticmethod
    def get_full_name(obj: User) -> str:
        return obj.full_name

    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password')
        read_only_fields = USER_READ_ONLY_FIELDS


class UserModelRegistrationSerializer(UserModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        label='Электронная почта'
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password], label='Пароль'
    )
    password2 = serializers.CharField(write_only=True, required=True, label='Подтверждение пароля')

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
        read_only_fields = USER_READ_ONLY_FIELDS
