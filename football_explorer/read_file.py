import sys
import codecs
from itertools import islice
counter = 0
file_counter = 1
with codecs.open("\\\\folder1\\folder2\\file1.tsv" , 'r', encoding='utf-8') as input_file:
        while True:
               nlines = list(islice(input_file, 1000000))
               outputf = codecs.open("\\\\folder1\\folder2\\file1" + str(file_counter) + ".tsv", 'w', encoding='utf-8')
               outputf.write(''.join(nlines))
               outputf.close()
               file_counter += 1
               if not nlines:
                        break
                    
import csv

def search(file):
  with open(file) as fp:
    for line in csv.reader(fp, delimiter='\t'):
      if line[0] == 'testing':
        raise StopIteration
      yield line[0]


for x in search('input.txt'):
  print(x)


