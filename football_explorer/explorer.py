import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, 'r') as fp:
            reader = csv.reader(fp, delimiter = ",")
            for line in reader:
                yield Player(*line)
        
    def search(self, country = None, year = None, age = None, position = None):
        if all([country == None, year == None, age == None, position == None]):
            raise ValueError('Provide search parameters')
            
        for player in self.all():
            if (not country or country == player.country and not year or year == player.year and not age or age == player.date_of_birth and not position or position == player.position):
                yield player
        