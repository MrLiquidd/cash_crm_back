from rest_framework import permissions, viewsets
from topics.api.serializers import TopicCategoryModelSerializer
from topics.models import TopicCategory


class TopicCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = TopicCategory.objects.all()
    serializer_class = TopicCategoryModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TopicCategory.objects.filter(personal_access=self.request.user)

    def perform_create(self, serializer):
        # Получаем переданного менеджера, если он указан
        manager_id = self.request.data.get('author', None)
        if manager_id:
            serializer.save(author_id=manager_id)
        else:
            # Или автоматически назначаем текущего пользователя в качестве менеджера
            serializer.save(manager=self.request.user)
