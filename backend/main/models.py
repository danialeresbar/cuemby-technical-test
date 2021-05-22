from django.db import models

# Team model constants
TEAM_NAME = 'name'
TEAM_VERBOSE_NAME = 'Team'
TEAM_VERBOSE_NAME_PLURAL = 'Teams'

# Player model constants
PLAYER_NAME = 'name'
PLAYER_NATION = 'nation'
PLAYER_POSITION = 'position'
PLAYER_TEAM = 'team'
PLAYER_TEAM_RELATED_NAME = 'players'
PLAYER_VERBOSE_NAME = 'Player'
PLAYER_VERBOSE_NAME_PLURAL = 'Players'


class Team(models.Model):
    """
    Team model class
    """

    name = models.CharField(max_length=128, unique=True, verbose_name=TEAM_NAME)

    class Meta:
        verbose_name = TEAM_VERBOSE_NAME
        verbose_name_plural = TEAM_VERBOSE_NAME_PLURAL

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    """
    Player model class
    """

    name = models.CharField(max_length=64, verbose_name=PLAYER_NAME)
    nation = models.CharField(max_length=64, verbose_name=PLAYER_NATION, blank=True)
    position = models.CharField(max_length=32, verbose_name=PLAYER_POSITION, blank=True)
    team = models.ForeignKey(
        Team,
        verbose_name=PLAYER_TEAM,
        related_name=PLAYER_TEAM_RELATED_NAME,
        on_delete=models.deletion.CASCADE
    )

    class Meta:
        verbose_name = PLAYER_VERBOSE_NAME
        verbose_name_plural = PLAYER_VERBOSE_NAME_PLURAL

    def __str__(self):
        return f'{self.name}'
