#!/usr/bin/env python

import django
import os
import requests
import sys

sys.path.append('/home/cuembyadm/app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cuemby.settings.development'
django.setup()

from main.models import Player, Team


def populate_database(players):
    for player in players:
        name = f"{player.get('firstName')} {player.get('lastName')}"
        nation = player.get('nation', dict()).get('name')
        position = player.get('position', '')
        team = player.get('club', dict()).get('name')
        team_object, _ = Team.objects.get_or_create(name=team)
        Player.objects.get_or_create(
            name=name,
            nation=nation,
            position=position,
            team=team_object
        )


if __name__ == '__main__':
    url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item?page='
    fut_request = requests.get(url=url + '1')

    try:
        response = fut_request.json()
        populate_database(response.get('items', list()))
        total_pages = response.get('totalPages', 1)
        for page in range(2, total_pages + 1):
            fut_request = requests.get(url=f'{url}{page}')
            response = fut_request.json()
            populate_database(response.get('items', list()))
    except Exception:
        response = fut_request.text
        print('Error')
