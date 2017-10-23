import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, 'r') as csvfile:
            player_reader = csv.reader(csvfile, delimiter=',')
            for row in player_reader:
                yield Player(*row)

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
            raise ValueError()

        players = self.all()
        for player in players:
            if ((not country or player.country == country)
                    and (not year or player.year == year)
                    and (not age or player.date_of_birth == age)
                    and (not position or player.position == position)):
                    yield player
