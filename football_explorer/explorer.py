import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return PlayerIterator(self.csv_file_name)

    def search(self, country=None, year=None, age=None, position=None):
        arglist = [country, year, age, position]
        if arglist.count(arglist[0]) == len(arglist):
            raise ValueError()
        else:
            return FilteredPlayerIterator(self.csv_file_name, arglist)


class PlayerIterator(object):
    def __init__(self, csv_fname):
        self.reader = csv.reader(open(csv_fname))
    
    def __iter__(self):
        return(self)

    def __next__(self):
        try:
            yay = next(self.reader)
        except StopIteration:
            raise StopIteration()
        return Player(*yay)

    def next(self):
        try:
            yay = next(self.reader)
        except StopIteration:
            raise StopIteration()
        return Player(*yay)
        

class FilteredPlayerIterator(PlayerIterator):
    def __init__(self, csv_fname, arglist):
        self.reader = csv.reader(open(csv_fname))
        self.arglist = arglist

    def __next__(self):
        try:
            yay = next(self.reader)
        except StopIteration:
            raise StopIteration()
        next_player = Player(*yay)
        player_args = [next_player.country, next_player.year, next_player.date_of_birth-next_player.year, next_player.position]
        conditions = [i for i, e in enumerate(self.arglist) if e != None]
        good = False
        for j in range(0,len(conditions)):
            good = (self.arglist[j] == player_args[j])
        if good == True:
            return next_player
        else:
            self.__next__()
        
    def next(self):
        try:
            yay = next(self.reader)
        except StopIteration:
            raise StopIteration()
        next_player = Player(*yay)
        player_args = [next_player.country, next_player.year, next_player.date_of_birth, next_player.position]
        conditions = [i for i, e in enumerate(self.arglist) if e != None]
        good = False
        for j in conditions:
            good = (self.arglist[j] == player_args[j])
        if good == True:
            print next_player.name          # the variable I am returning is a Player object
            return next_player              # but in tests.py, it says it is a NoneType object
        else:
            self.next()
