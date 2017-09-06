import csv
from .models import Player

class FileIterator(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.reader = None
        self.fp = None

    def __iter__(self):
        if not self.fp:
            self.fp = open(self.csv_file_name)
            self.reader = csv.reader(self.fp)
        return self

    def __next__(self):
        if self.fp.closed:
            raise StopIteration()
        try:
            line = next(self.reader)
            player = Player(*line)
            return player
        except StopIteration:
            self.fp.close()
            raise StopIteration()

    next = __next__

class FileSearch(object):
    def __init__(self, csv_file_name,country=None,year=None,age=None,position=None):
        self.csv_file_name = csv_file_name
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        self.fp = None
        self.reader = None

    def __iter__(self):
        self.fp = open(self.csv_file_name)
        self.reader = csv.reader(self.fp)
        return self

    def __next__(self):
        try:
            search_terms = []
            for value in self.country,self.year,self.age,self.position:
                if value is not None:
                    search_terms.append(value)
                    
            line = next(self.reader)
            player = Player(*line)
            
            match_found = False
            while not match_found:
                if set(search_terms) < set([player.country,player.year,player.position]):
                    match_found = True
                    return player
                else:
                    line = next(self.reader)
                    player = Player(*line)
                    continue
        except StopIteration:
            raise StopIteration()


    next = __next__


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return FileIterator(self.csv_file_name)


    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
            raise ValueError()

        return FileSearch(
            self.csv_file_name, country, year, age, position)