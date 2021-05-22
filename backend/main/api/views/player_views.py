from rest_framework import generics
from main.api.filters import NameFilterBackend, OrderFilterBackend
from main.api.serializers import PlayerSerializer
from main.api.pagination import CustomPagination

from backend.main.api.permissions import CustomPermission


class PlayerListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('name')
    filter_backends = (NameFilterBackend, OrderFilterBackend)
    permission_classes = (CustomPermission,)
