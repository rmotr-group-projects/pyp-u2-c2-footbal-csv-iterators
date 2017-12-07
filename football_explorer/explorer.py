import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, 'r') as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                yield player

    def __matches_search(self, player, country=None, year=None,
                         age=None, position=None):
        filter_values = [
            ('country', country),
            ('year', year),
            ('age', age),
            ('position', position),
        ]

        for field_name, value in filter_values:
            if value and getattr(player, field_name) != value:
                return False
        return True

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
            raise ValueError()

        for player in self.all():
            if self.__matches_search(player, country, year, age, position):
                yield player
