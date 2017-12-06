import csv
import os

from football_explorer.models import Player

"""
A row in the csv file is as follows:

No, Pos, Player, DOB/Age, Caps, Club, Country, ClubCountry, Year
0    1     2       3        4    5       6         7          8
"""

class FootballExplorer(object):
    """Explores a csv file containing football (soccer) data."""
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        if __name__ == '__main__':
            self.file_path = os.path.join('..', self.csv_file_name)
        else:
            self.file_path = self.csv_file_name

    def all_iterator(self):
        """Returns an iterator containing all the records from the csv file 
        as Player objects.
        """
        return FootballIterator(self.csv_file_name)
        
    def all(self):
        """Generator version of FootballExplorer.all()"""
        with open(self.file_path) as f:
            reader = csv.reader(f)
            for line in reader:
                yield Player(*line)

    def search_iterator(self, country=None, year=None, age=None, position=None):
        """Returns an iterator containing all the records from the csv file 
        matching the given parameters as Player objects.
        """
        str_year_and_age = self.__check_search_args(country, year, age, position)
        print(str_year_and_age)
        year = str_year_and_age['str_year']
        age = str_year_and_age['str_age']
        return FootballSearchIterator(self.csv_file_name, country, year, age, position)

    def search(self, country=None, year=None, age=None, position=None):
        """Generator version of FootballExplorer.search()"""
        str_year_and_age = self.__check_search_args(country, year, age, position)
        year = str_year_and_age['str_year']
        age = str_year_and_age['str_age']
        with open(self.file_path) as f:
            reader = csv.reader(f)
            for line in reader:
                if any([country and country != line[6], year and year != line[8], 
                        age and age != line[3], position and position != line[1]]):
                    continue
                yield(Player(*line))
            
    def __check_search_args(self, country, year, age, position):
        """Raise an exception if an invalid argument is provided, and return a 
        dictionary containing string versions of year and age.
        """
        # Not to be mistaken for FootballExplorer.all():
        if all([not country, not year, not age, not position]):
            raise ValueError("one of the parameters must be given a value.")
        if isinstance(year, int):
            year = str(year)
        if isinstance(age, int):
            age = str(age)
        # Python 2 has data type 'unicode' as well as 'str':
        if country and not isinstance(country, str) and not isinstance(country, unicode):
            raise ValueError('country must be type str or unicode (Python 2).')
        if year and not isinstance(year, int) and not isinstance(year, str):
            raise ValueError('year must be type str or int.')
        if age and not isinstance(age, int) and not isinstance(age, str):
            raise ValueError('age must be type str or int.')
        if position and not isinstance(position, str):
            raise ValueError('position must be type str.')
        return {'str_year': year, 'str_age': age}
            
class FootballIterator(FootballExplorer):
    def __init__(self, csv_file_name):
        super(FootballIterator, self).__init__(csv_file_name)
    
    def __iter__(self):
        self._file = open(self.file_path, )
        self._reader = csv.reader(self._file)
        return self
    
    def __next__(self):
        try:
            self._next_line = next(self._reader)
            return Player(*self._next_line)
        except StopIteration:
            self._file.close()
            raise StopIteration

    next = __next__
    
class FootballSearchIterator(FootballIterator):
    def __init__(self, csv_file_name, country=None, year=None, age=None, position=None):
        super(FootballSearchIterator, self).__init__(csv_file_name)
        self._country = country
        self._year = year
        self._age = age
        self._position = position
        
    def __next__(self):
        try:
            while True:
                self._next_line = next(self._reader)
                if any([self._country and self._country != self._next_line[6], 
                        self._year and self._year != self._next_line[8], 
                        self._age and self._age != self._next_line[3], 
                        self._position and self._position != self._next_line[1]]):
                    continue
                return Player(*self._next_line)
        except StopIteration:
            self._file.close()
            raise StopIteration
            
    next = __next__