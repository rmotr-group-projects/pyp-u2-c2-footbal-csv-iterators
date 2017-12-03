import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        raise NotImplementedError()

    def search(self, country=None, year=None, age=None, position=None):

        if not all([country, year, age, position]):
            raise ValueError
