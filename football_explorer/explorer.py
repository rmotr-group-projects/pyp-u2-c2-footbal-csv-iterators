import csv

from .models import Player

class FootballExplorer(Player):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        #################################################################
        #
        # all takes no parameters and should return an iterator that contains all the records from the csv file as Player objects.
        #
        #################################################################
        with open(self.csv_file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for line in reader:
                yield Player(*line)
    
    def search(self, country=None, year=None, age=None, position=None):
        #################################################################
        #
        # search four optional parameters: country, year, age, and position If none of these parameters are given it should raise a ValueError. 
        # The search method should return an iterator that contains all the records from the csv file that match the given parameters as Player objects.
        #
        #################################################################
        
        # Error if none are provided (any() returns True if any of the iunputs are True. In this case we are doing a NOT any())
        if not any([country, year, age]):
            raise ValueError()
        
        # Create iterable instance
        players = self.all()
        
        for p in players:
            if ( (p.country == country or not country) # if current line's country is equal to the parameter input's country OR if country is empty
                and (p.date_of_birth[-1:-3] == age or not age) # parse age from date of birth by getting last 3 characters
                and (p.year == year or not year)
                and (p.position == position or not position) ):
                    yield p # then return the row
        
        