import csv
from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                yield Player(*line)

    def search(self, player=None, country=None, year=None, age=None, position=None):
        search_values = [country, year, age, position]
        if not any(search_values):
            raise ValueError()
            
        for player in self.all():
            if self.search_player(player, country, year, age, position):
                yield player
    
    def search_player(self, player=None, country=None, year=None, age=None, position=None):
        search_values = {'country': country, 'year': year, 'age': age, 'position': position}
        
        for country, value in search_values.items():
            if value and getattr(player, country) != value:
                return False
        return True
        