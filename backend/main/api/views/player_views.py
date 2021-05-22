from rest_framework import generics
from main.api.filters import NameFilterBackend, OrderFilterBackend
from main.api.pagination import CustomPagination
from main.api.permissions import CustomPermission
from main.api.serializers import PlayerSerializer


class PlayerListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('name')  # Default order
    filter_backends = (NameFilterBackend, OrderFilterBackend)
    permission_classes = (CustomPermission,)
