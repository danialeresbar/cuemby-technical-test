from django.db import models

# Team model constants
TEAM_NAME = 'name'
TEAM_VERBOSE_NAME = 'Team'
TEAM_VERBOSE_NAME_PLURAL = 'Teams'

# Player model constants
PLAYER_NAME = 'name'
PLAYER_LAST_NAME = 'last_name'
PLAYER_NATIONALITY = 'nationality'
PLAYER_POSITION = 'position'
PLAYER_TEAM = 'team'


class Team(models.Model):
    """

    """

    name = models.CharField(max_length=128, unique=True, verbose_name=TEAM_NAME)

    class Meta:
        verbose_name = TEAM_VERBOSE_NAME
        verbose_name_plural = TEAM_VERBOSE_NAME_PLURAL

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    """

    """

    name = models.CharField(max_length=64, verbose_name=PLAYER_NAME)
    last_name = models.CharField(max_length=64, verbose_name=PLAYER_LAST_NAME)
    nationality = models.CharField(max_length=64, verbose_name=PLAYER_NATIONALITY, blank=True)
    position = models.CharField(max_length=32, verbose_name=PLAYER_POSITION, blank=True)
    team = models.ForeignKey(Team, verbose_name=PLAYER_TEAM, on_delete=models.deletion.CASCADE)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f'{self.name} {self.last_name}'
