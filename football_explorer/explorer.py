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
        # This generator calls the all() generator and searches through
        # the players recieved through that.
        for player in self.all():
            # Using this large if statement we can search the parameters given
            # whether it is one or all of them
            if (country and player.country != country or
                    year and player.year != year or
                    # Because they only have date of birth and age we split the
                    # string at age which is in the last few characters
                    age and int(player.date_of_birth[-3:-1]) != age or
                    position and player.position != position):
                # Using continue to skip the yield at the end of the method
                continue
            yield player
