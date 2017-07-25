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
                yield(player)
    
    def search(self, **kwargs):
        if len(kwargs) == 0:
            raise ValueError()
        return self._search(**kwargs)
    
    def _search(self, **kwargs):
        for player in self.all():
            if all([getattr(player, key) == kwargs[key] for key in kwargs]):
                yield player




