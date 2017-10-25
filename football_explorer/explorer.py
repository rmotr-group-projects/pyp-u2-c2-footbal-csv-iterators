import csv
from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
    # Using a generator to go through the file
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                yield Player(*line)

    def search(self, country=None, year=None, age=None, position=None):
        if not (country or year or age or position):
            raise ValueError()
        for player in self.all():
            if (country and player.country != country or
                    year and player.year != year or
                    age and player.age != age or
                    position and player.position != position):
                continue
            yield player
