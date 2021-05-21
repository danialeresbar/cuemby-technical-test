from rest_framework import generics
from main.api.filters import NameFilterBackend, OrderFilterBackend
from main.api.serializers import PlayerSerializer
from main.api.pagination import CustomPagination


class PlayerListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('name')
    filter_backends = (NameFilterBackend, OrderFilterBackend)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        if filters:
            search = filters.get('search', '')
            order = filters.get('order', 'asc')
            page = filters.get('page', 1)
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

