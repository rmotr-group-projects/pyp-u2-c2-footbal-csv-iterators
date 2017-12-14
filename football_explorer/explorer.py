import csv

from .models import Player

class FootballIterator(object):
    def __init__(self,csv_file_name):
        self.csv_file_name = csv_file_name
        self.fp = None
        self.csv_reader = None
        
    def __iter__(self):
        if not self.fp:
            self.fp = open(self.csv_file_name)
            self.csv_reader = csv.reader(self.fp)
        return self
        
    def __next__(self):
        if self.fp.closed:
            raise StopIteration()
        try:
            line = next(self.csv_reader)
            player = Player(*line)
            return player
            
        except StopIteration:
            self.fp.close()
            raise StopIteration()
        
    next = __next__
        
class FootballSearchIterator(FootballIterator):
    def __init__(self, csv_file_name, country=None, year=None, age=None, position = None):
        super(FootballSearchIterator, self).__init__(csv_file_name)
        
        self.csv_file_name = csv_file_name
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        
        self.filter_values = [{'field_name':'country','value':self.country},{'field_name':'year','value':self.year}, {'field_name':'age','value':self.age},{'field_name':'position','value':self.position}]
        
        def __matches(self, player):
            for filter_value in self.filter_values:
                field_name = filter_value['field_name']
                value = filter_values['value']
                if value and getattr(player, field_name)!= value:
                    return False
                return True
        
        def __next__(self):
            player=super(FootballSearchIterator,self).__next__()
            if self.__matches(player):
                return player
            return next(self)
            
        
        next = __next__


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        raise NotImplementedError()

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country,year,age,position]):
            raise ValueError()
        
        return FootballSearchIterator(self.csv_file_name,country, year, age, position)