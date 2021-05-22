import requests
from django.core.management import BaseCommand

from main.models import Player, Team

FUT21_BASE_URL = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page='


class Command(BaseCommand):
    help = 'Fetch data from fut21 API to populate the project DB'
    teams = list()

    @staticmethod
    def get_data():
        page = 1
        teams = list()
        players = list()

        while True:
            print(f'Fetching page: {page}')
            url = f'{FUT21_BASE_URL}{page}'
            page += 1

            try:
                response = requests.get(url).json()
            except Exception as e:
                print(f'Data for page {page} cannot be fetched')
                print(f'Error: {e}')
                break

            for player in response.get('items', list()):
                team = player.get('club', dict()).get('name')

                players.append({
                    'name': f"{player.get('firstName')} {player.get('lastName')}",
                    'nation': player.get('nation', dict()).get('name'),
                    'position': player.get('position', ''),
                    'team': team
                })

                teams.append(team)

            if page > response.get('totalPages'):
                break
        print('Fetch finished')

        teams_filtered = [{'name': team} for team in set(teams)]
        return players, teams_filtered

    def save_teams(self, teams):
        print('Saving teams found')
        self.teams = Team.objects.bulk_create(
            [Team(**team) for team in teams]
        )

    def save_players(self, players):
        print('Saving players found')
        # Initially, we need to map the team for any player
        for player in players:
            player['team'] = self.get_club_id_from_name(player['team'])

        Player.objects.bulk_create(
            [Player(**player) for player in players if player['team']]
        )

    def get_club_id_from_name(self, name):
        for team in self.teams:
            if team.name == name:
                return team

    def handle(self, *args, **kwargs):
        players, teams = self.get_data()
        self.save_teams(teams)
        self.save_players(players)
