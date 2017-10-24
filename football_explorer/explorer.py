import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return FootballIterator(self.csv_file_name)
            

    def search(self, **kwargs):
        #if not any ([country, year, age, position]):
        #    raise ValueError()
        if all([k not in kwargs for k in ['country', 'year', 'age', 'position']]):
            raise ValueError()
        return FilteredFootballIterator(self.csv_file_name, **kwargs)
        


class FootballIterator(object):
    def __init__(self, file_name):
        self.file_pointer = open(file_name)
        self.file_reader = csv.reader(self.file_pointer)
    def __iter__(self):
        return self
    def __next__(self):
        return Player(*next(self.file_reader))

    next = __next__
    
    def __del__(self):
        self.file_pointer.close()


class FilteredFootballIterator(FootballIterator):
    def __init__(self, file_name, **kwargs):
        super(FilteredFootballIterator, self).__init__(file_name)
        self.filter_dict = kwargs
    def __next__(self):

        foundPlayer = False
        nextPlayer = Player(*next(self.file_reader))
        while not foundPlayer:
            attrMismatch = False
            for filter_key, filter_value in self.filter_dict.items():
                if getattr(nextPlayer, filter_key) != filter_value:
                    attrMismatch = True
                    break
            if not attrMismatch:
                foundPlayer = True
            else:
                nextPlayer = Player(*next(self.file_reader))
        
        if foundPlayer:
            return nextPlayer
        else:
            self.file_pointer.close()
            self.file_pointer = None
            raise StopIteration()
    next = __next__
    