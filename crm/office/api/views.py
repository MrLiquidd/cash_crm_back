from rest_framework import viewsets

from office.models import Office
from office.api.serializer import OfficeModelSerializer


# Create your views here.
class OfficeModelViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = OfficeModelSerializer
    queryset = Office.objects.all()