import csv

from models import Player


class FootballIterator(object):
    def __init__(self, filename):
        self.filename = filename
        self.fp = open(self.filename)
        self.reader = csv.reader(self.fp)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            player = Player(*next(self.reader))
            return player
        except:
            self.fp.close()
            raise StopIteration()

    next = __next__


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return FootballIterator(self.csv_file_name)

    def search(self, country=None, year=None, age=None, position=None):
        if (country is None and year is None and age is None and
                position is None):
                    raise ValueError('Must provide country, year, age, or '
                                     'position')
