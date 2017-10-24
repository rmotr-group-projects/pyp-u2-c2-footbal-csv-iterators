import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        result = []
        
        lines = self.line_player
        
        try:
            for line in lines:
                yield Player(*line)
        except StopIteration:
            raise
    
    '''
        This function return a generator with file lines
    '''
    @property
    def line_player(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)

            for line in reader:
                yield line

    def search(self, country=None, year=None, age=None, position=None):
        result = []
        
        if country == None and year == None and age == None and position == None:
            raise ValueError()
        
        lines = self.line_player
        
        while True:
            try:
                line = next(lines) # Return the next item into iterator, using generator!
                player = Player(*line)
            
                if (country == player.country and not year) or\
                    (country == player.country and year == player.year) or\
                        (country == player.country and year == player.year and age == player.date_of_birth and position == player.position):
                    yield player
            except StopIteration:
                break
    
    
    
    
    
    
    
    
