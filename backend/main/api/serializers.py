from rest_framework import serializers
from main.models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    """
    Player model serializer
    """

    class Meta:
        model = Player
        exclude = ('id', 'team')


class TeamSerializer(serializers.ModelSerializer):
    """
    Team model serializer
    """

    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'players')
