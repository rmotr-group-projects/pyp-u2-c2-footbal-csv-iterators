import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, 'r') as f:
            all_players = []
            csvreader = csv.reader(f)
            for item in csvreader:
                all_players.append(Player(*item))
        return (all_players)    

    def search(self, country=None, year=None, age=None, position=None):
       if not any([country, year, age, position]):
             raise ValueError()
             
       search_dict = {'country': country, 'year': year, 'age': age, 'position': position } 
       
    #   for k,v in search_dict.items():
    #      if v is not None:
    #       with open(self.csv_file_name, 'r') as f:
    #          csvreader = csv.reader(f)
    #          fields = csvreader.next()
    #          match = []
    #          for item in csvreader:
    #              if item == 
   
   
    # def __iter__(self):
    #     return self
        
    # def __next__(self):
    #     pass
            
