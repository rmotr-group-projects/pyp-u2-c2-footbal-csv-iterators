import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def __iter__(self):
        self.file = open(self.csv_file_name)
        self.reader = csv.reader(self.file)
        return self

    def __next__(self):
        try:
            line = next(self.reader)
            player = Player(*line)
            return player
        except StopIteration:
            self.file.close()
            raise StopIteration()

    next = __next__

    def all(self):
        return self

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
            raise ValueError()
        search_params = {param: value for param, value in \
                        dict(locals()).items() if \
                        param !='self' and value is not None}
        return FootballSearch(self.csv_file_name, search_params)

class FootballSearch(FootballExplorer):
    def __init__(self, csv_file_name, search_params):
        super(FootballSearch, self).__init__(csv_file_name)
        self.search_params = search_params

    def check_player(self, other):
        for param, value in self.search_params.items():
            if getattr(other, param) != value:
                return False
        return True

    def __next__(self):
        while True:
            try:
                line = next(self.reader)
                player = Player(*line)
                if self.check_player(player):
                    return player
            except StopIteration:
                self.file.close()
                raise StopIteration()
