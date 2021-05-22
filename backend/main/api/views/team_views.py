from rest_framework import generics, response, views
from main.api.pagination import CustomPagination
from main.api.permissions import CustomPermission
from main.api.serializers import PlayerSerializer, Team, TeamSerializer


class TeamView(generics.GenericAPIView):
    pagination_class = CustomPagination
    permission_classes = (CustomPermission, )

    def post(self, request):
        self.check_permissions(request)
        name = request.data.get('Name', '')
        team = Team.objects.filter(name__icontains=name).order_by('name').first()
        players = PlayerSerializer.Meta.model.objects.filter(team=team).order_by('name')
        page = self.paginator.paginate_queryset(players, request)
        if page is not None:
            serializer = self.paginator.get_paginated_response(PlayerSerializer(page, many=True).data)
        else:
            serializer = PlayerSerializer(page)
        data = serializer.data
        return response.Response(data)
