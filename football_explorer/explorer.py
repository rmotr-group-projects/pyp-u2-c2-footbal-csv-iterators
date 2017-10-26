import csv
from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.player_list = self.all()
        
    def __iter__(self):
        with open(self.csv_file_name) as csvfile:
            csv_file = csv.reader(csvfile)
            self.row_count = sum(1 for row in csvfile)
        self.counter = 0
        return self
    
    
    def __next__(self):
        if self.counter < self.row_count:
            retrun_value = self.player_list[self.counter]
            self.counter += 1
            return retrun_value
        else:
            raise StopIteration
    
    next = __next__        
   
    def all(self):
        player_list = []
        with open(self.csv_file_name) as csvfile:
            csv_file = csv.reader(csvfile)
            for row in csv_file:
                player = Player(number=row[0],position=row[1], name=row[2], 
                date_of_birth = row[3], caps=row[4], club=row[5], 
                country=row[6], club_country=row[7], year=row[8])
                player_list.append(player)
        return player_list
    
    def search(self, country=None, year=None, age=None, position=None):
        
    
        if country == None and year == None and age == None and position == None:
            raise ValueError('No Search Category Provided')
        
        for player in self:
            player_country = player.country
            player_year = int(player.date_of_birth[1:5])
            player_age = int(player.date_of_birth[-3:-1])
            player_position = player.position
            if(country == None or country == player.country) and \
            (year == None or year == player.year) and \
            (age == None or age == player.age) and \
            (position == None or position == player.position):
                yield player
             

