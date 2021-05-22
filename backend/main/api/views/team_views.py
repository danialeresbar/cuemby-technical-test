from rest_framework import generics, response, views
from main.api.serializers import PlayerSerializer, Team, TeamSerializer
from main.api.pagination import PaginationHandlerMixin, CustomPagination
from main.api.permissions import CustomPermission


class TeamView(views.APIView, PaginationHandlerMixin):
    pagination_class = CustomPagination
    permission_classes = (CustomPermission, )

    def post(self, request, *args, **kwargs):
        self.check_permissions(request)
        name = request.data.get('Name', '')
        page = request.data.get('Page', 1)
        team = Team.objects.filter(name__icontains=name).order_by('name').first()
        players = PlayerSerializer.Meta.model.objects.filter(team=team).order_by('name')
        page = self.paginate_queryset(players)
        if page is not None:
            serializer = self.get_paginated_response(PlayerSerializer(page, many=True).data)
        else:
            serializer = PlayerSerializer(page)
        data =serializer.data
        return response.Response(data)


class TeamRetrieveView(generics.GenericAPIView):
    pagination_class = CustomPagination

    def post(self, request, *args, **kwargs):
        pass
