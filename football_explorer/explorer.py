import csv
from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as fname:
            self.fname_csv = csv.reader(fname)
            self.record_list = (Player(*line) for line in self.fname_csv)
            for player in self.record_list:
                yield player

    def search(self, **kwargs):
        if not any(kwargs.items()):
            raise ValueError
        '''
        for player in self.all():
            if all([getattr(player, key) == val for key, val in kwargs.items()]):
                yield player
        '''
        return (player for player in self.all() if all([getattr(player, key,'') == val for key, val in kwargs.items()]))