from rest_framework import generics, filters
from main.api.serializers import PlayerSerializer
from main.api.pagination import CustomPagination


class PlayerListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('name')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

