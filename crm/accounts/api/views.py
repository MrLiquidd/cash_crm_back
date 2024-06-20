from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import User
from accounts.api.serializers import UserModelSerializer, UserModelRegistrationSerializer


class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    registration_serializer_class = UserModelRegistrationSerializer

    @extend_schema(
        methods=('post', ),
        request=registration_serializer_class,
        responses={status.HTTP_201_CREATED: registration_serializer_class},
        description="Регистрация пользователя"
    )
    @action(detail=False, methods=('post', ), url_path='signup', permission_classes=(AllowAny, ))
    def signup(self, request):
        serializer = self.registration_serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)

    @action(detail=False, methods=('get', 'patch', 'put'), url_path='me')
    def me(self, request):
        serializer = self.serializer_class(instance=request.user, data=request.data)
        if serializer.is_valid(raise_exception=True) and request.method.lower() in ('put', 'patch'):
            serializer.save()
        return Response(data=serializer.data)
