import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.iter = FootballIter(csv_file_name)

    def all(self):
        return self.iter

    def search(self, country=None, year=None, age=None, position=None):
        attributes = {
            'country': country,
            'year': year,
            'age': age,
            'position': position
        }

        # function will short circuit if a single non-None value is found
        if all([value is None for value in attributes.values()]):
            raise ValueError()

        return FootballFilter(FootballIter(self.csv_file_name), attributes)


class FootballIter(object):

    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.reader = None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.reader is None:
                fp = open(self.csv_file_name)
                self.reader = csv.reader(fp)
            return Player(*next(self.reader))
        except StopIteration:
            raise StopIteration()

    next = __next__


class FootballFilter(object):
    def __init__(self, iterator, attributes):
        self.iterator = iterator
        self.attributes = attributes

    def __iter__(self):
        return self

    def __next__(self):
        try:
            player = next(self.iterator)
            while not self.is_match(player):
                player = next(self.iterator)
            return player
        except StopIteration:
            raise StopIteration()

    def is_match(self, player):
        return all(value is None or getattr(player, key) == value for key, value in self.attributes.items())
