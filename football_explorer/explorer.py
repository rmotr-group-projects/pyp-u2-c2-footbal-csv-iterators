import csv

from .models import Player


class FootballExplorer(object):
    """
    Public interface for exploring a CSV file of football players
    """

    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.iter = FootballCsvIterator(csv_file_name)

    def all(self):
        return self.iter

    def search(self, country=None, year=None, age=None, position=None):
        attributes = {
            'country': country,
            'year': year,
            'age': age,
            'position': position
        }

        # Conditional will short circuit if a single non-None value is found
        if all([value is None for value in attributes.values()]):
            raise ValueError()

        return FootballFilter(self.iter, attributes)


class FootballCsvIterator(object):

    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.reader = None

    def __iter__(self):
        return self

    def __next__(self):
        # We attempt to load the data from the csv lazily so we
        # don't have to store it in a local data structure
        try:
            # instantiate the reader if this is the first query,
            # otherwise use the open instance
            if self.reader is None:
                self.fp = open(self.csv_file_name)
                self.reader = csv.reader(self.fp)
            return Player(*next(self.reader))
        except StopIteration:
            # TODO: I don't actually know if this is safe, is there a guarantee this will execute?
            self.fp.close()
            raise StopIteration()

    next = __next__


class FootballFilter(object):
    """
    Used when the client wishes to filter the players to iterate though based
    on given criteria, uses the above defined iterator for lazy evaluation
    """

    def __init__(self, iterator, attributes):
        self.iterator = iterator
        self.attributes = attributes

    def __iter__(self):
        return self

    def __next__(self):
        player = next(self.iterator)
        while not self.is_match(player):
            player = next(self.iterator)
        return player

    next = __next__

    def is_match(self, player):
        """
        Returns true if all search attributes match the player
        parameter or the search attribute is not given
        """
        return all(value is None or
                   getattr(player, key) == value for key, value in self.attributes.items())
