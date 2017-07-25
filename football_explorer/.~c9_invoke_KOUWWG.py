import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        '''
        takes no parameters and should return an iterator that contains all the records from the csv file as Player objects.
        '''
        return self
        # raise NotImplementedError()

    def search(self, country=None, year=None, age=None, position=None):
        raise NotImplementedError()

