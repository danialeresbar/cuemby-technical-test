from rest_framework import generics, filters
from main.api.serializers import PlayerSerializer


class PlayerListView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
