import csv

from .models import Player


class FootballIterable(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.fp = open(self.csv_file_name )
        self.index = csv.reader(self.fp)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            line = next(self.index)
            player = Player(*line)
            return player
        except StopIteration:
            self.fp.close()
            raise StopIteration()

    next = __next__


class FootballSearchIterable(FootballIterable):
    def __init__(self, csv_file_name, country=None, year=None, age=None, position=None):
        super(FootballSearchIterable, self).__init__(csv_file_name)
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        

    def _matched(self, player):
        if (self.country and self.country != player.country) or \
                (self.year and self.year != player.year) or \
                (self.age and self.age != player.age) or \
                (self.position and self.position != player.position):
            return False
        return True
        
    def __next__(self):
        player = super(FootballSearchIterable, self).__next__()
        if self._matched(player):
            return player
        return next(self)

    next = __next__

# class FootballSearchIterable(object):
#     def __init__(self, csv_file_name, country=None, year=None, age=None, position=None, all=None):
#         self.csv_file_name = csv_file_name
#         self.country = country
#         self.year = year
#         self.age = age
#         self.position = position
#         self._all = all
        
#     def __iter__(self):
#         return self

#     def _matched(self, player):
#         if (self.country and self.country != player.country) or \
#                 (self.year and self.year != player.year) or \
#                 (self.age and self.age != player.age) or \
#                 (self.position and self.position != player.position):
#             return False
#         return True
        
#     def __next__(self):
#         player = self._all.next()
#         if self._matched(player):
#             return player
#         return next(self)
    
#     next = __next__


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return FootballIterable(self.csv_file_name)

    def search(self, country=None, year=None, age=None, position=None):
        if country==None and year==None and age==None and position==None:
            raise ValueError()
        return FootballSearchIterable(self.csv_file_name, country, year, age, position)
        # return FootballSearchIterable(self.csv_file_name, country, year, age, position, self.all())        
        
        



