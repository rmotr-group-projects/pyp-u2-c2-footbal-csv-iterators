import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.file = None
        self.reader = None
        #self.country = None
        #self.age = None
        #self.year = None
        #self.position = None
        
    def __iter__(self):
        #if not self.file:
        self.file = open(self.csv_file_name)
        self.reader = csv.reader(self.file)
        return self
    '''        
    def __next__(self):
        try:
            line = next(self.reader)
            player = Player(*line)
            return player
        except:
            raise StopIteration()

    def all(self):
        return self

    next = __next__

class FootballSearch(FootballExplorer):
    def __init__(self, csv_file_name):
        super().__init__(csv_file_name)
    '''
    def __next__(self):
        try:
            line = next(self.reader)
            player = Player(*line)
            if self.check_player(player):
                return player
            return next(self)
        except:
            raise StopIteration()
        
    next =__next__
    
    def check_player(self, other):
        for k, v in self.search_params.items():
            if getattr(other, k) != v:
                return False
        return True
    
    def search(self, country=None, year=None, age=None, position=None):
        if all([country==None, year==None, age==None, position==None]):
        #alternatively
        #if not any([country, year, age, position]):
            raise ValueError()
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        self.search_params = {k: v for k, v in dict(locals()).items() if k!='self' and v != None}
        return self
