from rest_framework import generics, filters
from main.api.serializers import TeamSerializer


class TeamListView(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
