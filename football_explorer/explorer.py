import csv

from .models import Player

class PlayerIterator(object):
    
    def __init__(self, players):
        self.players = players
        self.index = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.players):
            raise StopIteration()
            
        elem = self.players[self.index]
        self.index += 1
        return elem
            
    next = __next__
    

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.players = self.load_file()

    def load_file(self):
        players = []
        with open(self.csv_file_name, 'r') as f:
            for line in f:
                items = line.split(',')
                player = Player(items[0], items[1], items[2], items[3], 
                                items[4], items[5], items[6], items[7], 
                                items[8])
                players.append(player)
        
        return players
    
    def all(self):
        return PlayerIterator(self.players)

    def search(self, country=None, year=None, age=None, position=None):
        if (country or year or age or position) == None:
            raise ValueError()
            
        return [player for player in self.all()
                if (country == player.country or not country) and
                   (year == player.year or not year) and 
                   (age == player.date_of_birth[-3:-1] or not age) and
                   (position == player.position or not position)]