import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        playersList = []
        with open(self.csv_file_name, 'r') as fp:
            for row in fp:
                playerInfo = row.split(',')
                playerObj = Player(number = playerInfo[0], position = playerInfo[1], 
                    name = playerInfo[2], date_of_birth = playerInfo[3], caps = playerInfo[4], 
                    club = playerInfo[5], country = playerInfo[6], club_country = playerInfo[7], year = playerInfo[8])
                playersList.append(playerObj) 
                
        return playersList                            
        

    def search(self, country=None, year=None, age=None, position=None):
        if country is None and year is None
            r
