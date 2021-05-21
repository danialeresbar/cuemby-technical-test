from rest_framework import response, views
from main.api.serializers import PlayerSerializer, Team, TeamSerializer
from main.api.pagination import PaginationHandlerMixin, CustomPagination


class TeamView(views.APIView, PaginationHandlerMixin):
    pagination_class = CustomPagination

    def post(self, request):
        name = request.data.get('Name', '')
        team = Team.objects.filter(name__icontains=name).order_by('name').first()
        players = PlayerSerializer.Meta.model.objects.filter(team=team).order_by('name')
        page = self.paginate_queryset(players)
        if page is not None:
            serializer = self.get_paginated_response(PlayerSerializer(page, many=True).data)
        else:
            serializer = PlayerSerializer(page)
        data =serializer.data
        return response.Response(data)
