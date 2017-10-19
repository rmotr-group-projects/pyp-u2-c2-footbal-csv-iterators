import csv

from .models import Player

#It may make things easier to create a base iterator class for returning all records and then have a child class inherit from that for handling filtering search results.

'''
with open('squads.csv') as fp:
    reader = csv.reader(fp)
    for line in reader:
        player = Player(*line)
        print(player)
'''

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        new_player = lambda x: Player(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        all_footballers = []
        
        f = open(self.csv_file_name)
        footballers = csv.reader(f)
        for footballer in footballers:
            all_footballers.append(new_player(footballer))
        return all_footballers

    def search(self, country=None, year=None, age=None, position=None):
        # If none of these parameters are given it should raise a ValueError
        # return an iterator that contains all the records from the csv file that match the given parameters as Player objects
        raise NotImplementedError()