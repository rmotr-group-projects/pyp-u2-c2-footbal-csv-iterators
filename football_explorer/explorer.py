import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.players = []
        self.idx = 0

    def __iter__(self):
        self.read_csv()
        self.idx = 0
        return self.players

    def read_csv(self):
        with open(self.csv_file_name, newline='') as csvfile:
            fields = ["number","position","name","date_of_birth","caps","club","country","club_country","year"]
            reader = csv.reader(csvfile,fieldnames=fields,delimiter=',')
            for row in reader:
                new_player = Player(row.number,row.position,row.name,row.date_of_birth,row.caps,row.club,row.country,row.club_country,row.year)
                self.players.append(new_player)

    def __next__():
        if self.idx + 1 > len(players):
            raise StopIteration
        player = self.players[self.idx]
        self.idx += 1
        return player


    def all(self):
        return self.__iter__()

    def search(self, country=None, year=None, age=None, position=None):
        raise NotImplementedError()
