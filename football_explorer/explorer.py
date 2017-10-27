import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return PersonsIterator(self.csv_file_name)

    def search(self, country=None, year=None, age=None, position=None):
        if not any([country,year,age,position]):
            raise ValueError
        return SearchIterator(self.csv_file_name,country,year,age,position)

class PersonsIterator(object):
    def __init__(self,csv_file_name):
        self.players = []
        self.idx = 0
        self.csv_file_name = csv_file_name

    def __iter__(self):
        self.players = []
        self.idx = 0
        self.read_csv()
        return self

    def read_csv(self):
        with open(self.csv_file_name) as csvfile:
            fields = ["number","position","name","date_of_birth","caps","club","country","club_country","year"]
            reader = csv.DictReader(csvfile,fieldnames=fields,delimiter=',')
            for row in reader:
                new_player = Player(row['number'],
                                    row['position'],
                                    row['name'],
                                    row['date_of_birth'],
                                    row['caps'],
                                    row['club'],
                                    row['country'],
                                    row['club_country'],
                                    row['year'])
                self.players.append(new_player)

    def __next__(self):
        if self.idx + 1 > len(self.players):
            raise StopIteration
        player = self.players[self.idx]
        self.idx += 1
        return player

    next = __next__

class SearchIterator(PersonsIterator):
    def __init__(self, filename, country=None, year=None, age=None, position=None):
        self.filters  =  {
            'country' : country,
            'year' : year,
            'age' : age,
            'position' : position
        }

        super(SearchIterator, self).__init__(filename)

    def search_by_terms(self,player):
        for key, value in self.filters.items():
            if value and getattr(player, key) != value:
                return False
        return True

    def __next__(self):
        player = super(SearchIterator, self).__next__()
        if self.search_by_terms(player):
            return player
        return next(self)

    next = __next__
