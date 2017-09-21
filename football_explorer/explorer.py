import csv

from .models import Player

class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                yield player
    
    def search(self, **kwargs):
        '''
        forces ValueError to be raised before _self.next() is callled 
        '''
        if not any (kwargs):
            raise ValueError()
        else:
            return self._search(**kwargs)
            
    def _search(self, **kwargs):
        for player in self.all():
            valid_match = True
            for key in kwargs:
                if key and getattr(player, key) != kwargs[key]:
                    # print("{}:{}".format(key, kwargs[key]))
                    valid_match = False
                    break
            if valid_match:
                yield player

# explorer = FootballExplorer(csv_file_name='/home/ubuntu/workspace/test_data.csv')
# results = explorer.all()
# print(results.next())

# print(results)
# for player in results:
    # print(player.year)
# iterator = iter(results) # what is this ? how is it diff from results?
# print(iterator)

# srch = explorer.search(country='Brazil', year=2010)
# print(srch)
# for player in srch:
#     print('{} {}'.format( player ,player.year))

