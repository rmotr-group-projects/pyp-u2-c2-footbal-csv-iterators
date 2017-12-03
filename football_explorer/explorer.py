import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        """
        Yields the Player object with each yield (defined in models.py)
        """

        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                yield Player(*line)

    def search(self, country=None, year=None, age=None, position=None):
        """
        Yields the Player object the matches search criteria
        """

        search_criteria = [country, year, age, position]

        if not any(search_criteria):
            raise ValueError

        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:

                player = Player(*line)

                player_attribute = [player.country,
                                    player.year,
                                    player.date_of_birth,
                                    player.position]

                # check if criteria equal attribute only for criteria that were provided
                search_restriction = [(criteria == attribute)
                                      for criteria, attribute in zip(search_criteria, player_attribute)
                                      if criteria]

                if all(search_restriction):
                    yield player
