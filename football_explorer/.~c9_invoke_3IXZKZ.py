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


    def keep_player(self, country, year, player):
        #return True if player object contains defined parameters 
        param_values = {
            'year':year,
            'country':country,
            #'age':age,
            #'position':position
        }
        
        params = ['country', 'year'] #, 'age', 'position'
            if self.filter(player.country, player.year, player.age, se)
        for param in params:
            value = param_values[param]
            if value and getattr(player, param) != value:
                r
        return True
        
        #return False
    
    def search(self, country=None, year=None):
        for player in self.all():
            if self.keep_player(player.country, player.year, player):
                yield player
        #raise StopIteration()


'''
def keep_it(player, year=None, country=None, age=None)
    param_values = {
        'year': year,
        'country': country,
        'age': age
    }

    params_to_check = ['country', 'year', 'age']
    for param in params_to_check:
        value = param_values[param]
        if value and getattr(player, param) != value:
            return False

    return False
    

def search(self, year, country):
    for player in self.all():
        if self.keep_it(player, year, country):
            yield player
    raise StopIteration()
'''