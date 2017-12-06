import csv

from .models import Player


class PlayerIter(object):
    def __init__(self, players_csv):
        self.players_csv = players_csv
        self.index = 0
        
    def player_files(self): 
        players = []
        with open(self.players_csv) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader: 
                player = Player(*line)
                yield player
       
            
        #return players
                
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.index >= len(self.players_csv): 
            raise StopIteration()
        player = self.players_csv[self.index]
        self.index += 1 
        return player
    
    next = __next__
    
class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        play_iter = PlayerIter(self.csv_file_name)
        return play_iter.player_files()

    def search(self, country=None, year=None, age=None, position=None):
        player_res = []
        attributes = [country, year, age, position]
        if not any(attributes): 
            raise ValueError()
            
        for player in self.all():
            if ((player.country == country or not country) and (player.year == year or not year) and (player.date_of_birth[-3:-1] == age or not age) and (player.position == position or not position)):
                yield player
