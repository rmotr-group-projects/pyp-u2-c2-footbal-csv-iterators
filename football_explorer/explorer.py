import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        
    def all(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                yield player
        
        
    def search(self, **kwargs):
        if len(kwargs) == 0:
            raise ValueError
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                if all([getattr(player, key) == kwargs[key] for key, value in kwargs.items()]):
                    yield player

