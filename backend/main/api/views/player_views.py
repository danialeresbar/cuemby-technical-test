from rest_framework import generics, response, status
from main.api.filters import NameFilterBackend, OrderFilterBackend
from main.api.serializers import PlayerSerializer
from main.api.pagination import CustomPagination
from main.api.throttles import CustomThrottle


class PlayerListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('name')
    filter_backends = (NameFilterBackend, OrderFilterBackend)
