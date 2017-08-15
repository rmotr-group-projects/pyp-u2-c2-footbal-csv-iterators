import csv

from .models import Player


class BaseIteratorClass(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.players = []
        
    def all(self):
        '''Turns player data from the csv file into player objects'''
        
        with open(self.csv_file_name) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                player = Player(*line)
                self.players.append(player)
            return self.players
                
    def __iter__(self):
        self.count = 0
        return self
        
    def __next__(self):
        if self.count >= len(self.players):
            raise StopIteration
        player = self.players[self.count]
        self.count += 1
        return player
    
    next = __next__


class FootballExplorer(BaseIteratorClass):

    def search(self, country=None, year=None, age=None, position=None):
        '''
        Searches all the players from the CSV file that match
        search criteria. Must have at least one of the following:
        country, year, age, or position.
        '''
        
        if country == None and year == None and \
                            age == None and position == None:
            raise ValueError
            
        self.all()
        
        def check_country(country, player):
            if country:
                if player.country == country:
                    return True
                elif player.country != country:
                    return False
            return True
                        
        def check_year(year, player):
            if year:
                if player.year == year:
                    return True
                elif player.year != year:
                    return False
            return True
                        
        def check_age(age, player):
            if age:
                if player.age == age:
                    return True
                elif player.age != age:
                    return False
            return True
                        
        def check_position(position, player):
            if position:
                if player.position == position:
                    return True
                elif player.position != position:
                    return False
            return True
                        
        self.search_results = []
        
        for player in self.players:
            if check_country(country, player) and check_year(year, player) \
            and check_age(age, player) and check_position(position, player):
                self.search_results.append(player)
                        
        return self.search_results

