import csv

from models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, 'r') as f:
            csvreader = csv.reader(f)
            for item in csvreader:
                yield Player(*item)
       
    def search(self, country=None, year=None, age=None, position=None):
        if not any([country, year, age, position]):
             raise ValueError()
        
        search_string = []
        for val in (country,year,age,position):
            if val is not None:
               search_string.append(str(val))
      
        with open(self.csv_file_name, 'r') as f:
          csvreader = csv.reader(f)
          for item in csvreader:
            if all(word in item for word in search_string):    
                yield (Player(*item))
     
   
