import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        return BaseIter(self.csv_file_name)

    def search(self, country=None, year=None, age=None, position=None):
        self.country = country
        self.year = year
        self.age = age
        self.position = position
        if all(arg is None for arg in [self.country, self.year, self.age, self.position]):
            raise ValueError
        else:
            return SearchIter(self.csv_file_name, self.country, self.year, self.age, self.position)

class BaseIter(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        
    def __iter__(self):
        opened_csv = open(self.csv_file_name)
        self.reader = csv.reader(opened_csv)
        return self
    
    def __next__(self):
        row = next(self.reader)
        player = Player(*row)
        return player
    
    next = __next__
        
class SearchIter(BaseIter):
    def __init__(self, csv_file_name, country, year, date_of_birth, position):
        super(SearchIter, self).__init__(csv_file_name)
        if year is not None:
            year = str(year)
        if date_of_birth is not None:
            date_of_birth = '(aged {})'.format(date_of_birth)
            print(date_of_birth)
        self.dict = {
            'country': country,
            'year': year, 
            'date_of_birth': date_of_birth,
            'position': position
        }
        
    def __next__(self):
        while True:
            player = super(SearchIter, self).__next__()
            if all(self.dict[key] in str(getattr(player, key)) for key, value in {k:v for k, v in self.dict.items() if v is not None}.items()):
                break
        return player
 
    next = __next__