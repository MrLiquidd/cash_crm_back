from rest_framework import permissions, viewsets
from topics.api.serializers import TopicCategoryModelSerializer
from topics.models import TopicCategory


class TopicCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = TopicCategory.objects.all()
    serializer_class = TopicCategoryModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TopicCategory.objects.filter(personal_access=self.request.user)
