import csv
from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as csvfile:
            for row in csv.reader(csvfile):
                yield Player(*row)

    def search(self, country=None, year=None, age=None, position=None):
        if not country and not year and not age and not position:
            raise ValueError

