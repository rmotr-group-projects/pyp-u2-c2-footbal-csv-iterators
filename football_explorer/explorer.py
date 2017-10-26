import csv
from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as f:
            footballers = csv.reader(f)
            for footballer in footballers:
                yield Player(*footballer)

    def search(self, country=None, year=None, age=None, position=None):
        search_args = locals()
        player_attr = {
            'country': 'country',
            'year': 'year',
            'age': 'date_of_birth',
            'position': 'position'
        }
        filter_dict = {player_attr[key]: search_args[key] for key in player_attr if search_args[key] is not None}
        
        if not filter_dict:
            raise ValueError()
        for footballer in self.all():
            if all([getattr(footballer, arg) == filter_dict[arg] for arg in filter_dict]):
                yield footballer
