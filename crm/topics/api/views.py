from rest_framework import permissions, viewsets
from topics.api.serializers import TopicModelSerializer
from topics.models import Topic


class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset
        return qs.filter()

    def perform_create(self, serializer):
        manager_id = self.request.data.get('author', None)
        if manager_id:
            serializer.save(author_id=manager_id)
        else:
            # Или автоматически назначаем текущего пользователя в качестве менеджера
            serializer.save(manager=self.request.user)
