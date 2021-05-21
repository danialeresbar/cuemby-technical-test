from rest_framework import serializers
from main.models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('id', )


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ('name', 'players')
