import csv
from football_explorer.models import Player


#with open(fname) as fp:
#    reader = csv.reader(fp)
#
#    for line in reader:
#        player = Player(*line)
#        print(player)

#    for i in range(100000):
#       line = next(reader)
#       print Player(*line)


class PlayerIterator(object):
    def __init__(self, csv_fname):
        self.reader = csv.reader(open(csv_fname))

    def __iter__(self):
        return(self)

    def __next__(self):
        print 'YAY'
        try:
            yay = next(self.reader)
        except StopIteration:
            raise StopIteration()
        return Player(*yay)

class FilteredPlayerIterator(PlayerIterator):
    def __init__(self, csv_fname, arglist):
        self.reader = csv.reader(open(csv_fname))
        self.arglist = arglist

    def __next__(self):
        print 'YAY'
        try:
            yay = next(self.reader)
            print Player(*yay).name
        except StopIteration:
            raise StopIteration()
        next_player = Player(*yay)
        player_args = [next_player.country, next_player.year, next_player.date_of_birth, next_player.position]
        print player_args
        conditions = [i for i, e in enumerate(self.arglist) if e != None]
        good = False
        for j in range(0,len(conditions)):
            good = (self.arglist[j] == player_args[j])
            print player_args[j]
        if good == True:
            print 'nope'
            return next_player
        else:
            print 'oops'
            self.__next__()
        

        
        
fname = 'test_data.csv'
arglist = ['Brazil', None, None, None]

myiter = FilteredPlayerIterator(fname, arglist)

yay = myiter.__next_()
#print yay.country
#print yay.name

#conditions = [0 if (i == None) else 1 for i in arglist]

#conditions = [i for i, e in enumerate(arglist) if e != None]
#for j in range(0,len(conditions)):
#    print (arglist[j] == conditions[j])


#if arglist.count(arglist[0]) == len(arglist):
#    print 'no'
#else:
#    print 'yes'


