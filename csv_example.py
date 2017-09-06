import csv
from football_explorer.models import Player


with open('test_data.csv') as fp:
    reader = csv.reader(fp)
    for line in reader:
        player = Player(*line)
        print(player)






