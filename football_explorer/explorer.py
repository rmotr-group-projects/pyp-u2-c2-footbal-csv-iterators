import csv

from .models import Player

class SearchIterator(object):
    def __init__(self, csv_file_name, country= None, year = None, age = None, position = None):
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        self.csv_file_name = csv_file_name
        self.OpenFile = open(self.csv_file_name)
        self.fileReader = csv.reader(self.OpenFile)
        
    def isMatch(self, player):
        if (self.country and getattr(player, 'country') != self.country):
            return False
            
        if (self.year and getattr(player, 'year') != self.year):
            return False
            
        if (self.age and getattr(player, 'age') != self.age):
            return False
            
        if (self.position and getattr(player, 'position') != self.position):
            return False
            
        return True
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.OpenFile.closed:
            raise StopIteration()
        try:
            line = (next(self.fileReader))
            self.player = Player(*line)
            if self.isMatch(self.player):
                return self.player
            return self.next()
                
        except StopIteration:
            self.OpenFile.close()
            raise StopIteration()
            
    next = __next__
        

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        self.OpenFile = open(self.csv_file_name)
        self.fileReader = csv.reader(self.OpenFile)
        self.PlayerList = []
        self.moreLines = True
        while self.moreLines:
            try:
                line = (next(self.fileReader))
                self.player = Player(*line)
                self.PlayerList.append(self.player)
            except StopIteration:
                self.OpenFile.close()
                self.moreLines = False
        return(self.PlayerList)
                
            
            

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
            raise ValueError()
        return SearchIterator(
            self.csv_file_name, country, year, age, position)
