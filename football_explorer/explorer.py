import csv

from .models import Player
        
class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def _read_csv(self):
        reader = csv.reader(open(self.csv_file_name))
        for row in reader:
            # result is going to be the rows provided by read_csv, not a single row
            player = Player(*row)
            yield player
    
    def all(self):
        # remember, this is a generator, you need to iterate over it
        generator_object = self._read_csv() 
        player_generator = iter(generator_object)
        
        while True:
            yield next(player_generator) 


    def search(self, country=None, year=None, date_of_birth=None, position=None):
        
        if not any ([country, year, date_of_birth, position]):
            raise ValueError
        
        generator_object = self._read_csv() 
        player_generator = iter(generator_object)
        
            
        while True:
            player = next(player_generator)
                
            if ((player.country == country or country == None) and (player.year    == year    or year    == None) and (player.date_of_birth == date_of_birth or date_of_birth == None) and (player.position == position or position == None)):
                    
                yield player
                
