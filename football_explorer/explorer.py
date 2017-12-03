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

                print(*line)

                yield Player(*line)

    def search(self, country=None, year=None, age=None, position=None):
        """
        Yields the Player object the matches search criteria
        """

        player_attr = [country, year, age, position]

        if not any(player_attr):
            raise ValueError

        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:

                player = Player(*line)

                player_attr_line = [player.country,
                                    player.year,
                                    player.date_of_birth,
                                    player.position]

                search_restriction = [(pa == pal) for pa, pal in zip(player_attr, player_attr_line) if pa]

                if all(search_restriction):
                    print(*line)
                    yield player
