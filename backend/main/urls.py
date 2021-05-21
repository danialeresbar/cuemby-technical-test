from django.urls import include, path

from main.api.views.player_views import PlayerListView
from main.api.views.team_views import TeamView


apiurls = [
    path('players', PlayerListView.as_view()),
    path('team/', TeamView.as_view())
]
