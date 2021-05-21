from django.urls import include, path

from main.api.views.player_views import PlayerListView
from main.api.views.team_views import TeamListView


apiurls = [
    path('players', PlayerListView.as_view()),
    path('teams', TeamListView.as_view())
]
