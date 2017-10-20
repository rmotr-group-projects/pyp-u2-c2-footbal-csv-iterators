import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as f:
            footballers = csv.reader(f)
            all_footballers = []
            for footballer in footballers:
                all_footballers.append(Player(*footballer))
        return all_footballers

    def search(self, country=None, year=None, age=None, position=None):
        search_args = locals()
        player_idx = {
          'country': 6,
          'year':8,
          'age':3,
          'position':1
        }
        filter_dict = {player_idx[key]: search_args[key] for key in player_idx if search_args[key] is not None}
        
        if not filter_dict:
            raise ValueError()
        with open(self.csv_file_name) as f:
            footballers = csv.reader(f)
            matched_footballers = []
            for footballer in footballers:
                if all([footballer[f_key] == str(filter_dict[f_key]) for f_key in filter_dict]):
                    matched_footballers.append(Player(*footballer))
        return matched_footballers
