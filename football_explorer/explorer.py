import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
   

    def all(self):
        with open(self.csv_file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for line in reader:
                yield Player(*line)
        

    def search(self, country = None, year = None, age = None, position = None):
        
        if not country and not year and not age and not position:
            raise ValueError('Provide at least one search value!')
        
        for player in self.all():
            if ((not country or player.country == country)
                    and (not year or player.year == year)
                    and (not age or player.date_of_birth == age)
                    and (not position or player.position == position)):
                    yield player
