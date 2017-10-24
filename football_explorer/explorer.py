import csv

from .models import Player

class ContextManager():
  def __init__(self,filename,mode):
    self.filename = filename
    self.mode = mode
    
  def __enter__(self):
    self.open_file = open(self.filename, self.mode)
    return self.open_file
    
  def __exit__(self, *args):
    self.open_file.close()

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with ContextManager('test_data.csv', 'r') as f:
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
      
        with ContextManager('test_data.csv', 'r') as f:
          csvreader = csv.reader(f)
          for item in csvreader:
            if all(word in item for word in search_string):    
                yield (Player(*item))
     
   
