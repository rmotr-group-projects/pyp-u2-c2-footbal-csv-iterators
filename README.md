Football Iterators
=============== 
Today we will be building a custom iterator. We are going to create a program for searching football(soccer) statistics from within a CSV(comma separated values) file. 
We will be using Python's builtin CSV module for handling file processing duties, documentation available here: https://docs.python.org/3/library/csv.html 
**Note:** There is an example for basic csv reading listed under the `reader` method.

Your code will reside in the #`explorer.py` file, the `models.py` file is provided for you and does not need to be altered.

The public interface to your program will be the `FootballExplorer` class. The `__init__` for this class takes a single parameter, the filename for the csv file to read.
The class should also have two methods as part of its public interface:  `all` and `search`

`all` takes no parameters and should return an iterator that contains all the records from the csv file as Player objects.

`search` four optional parameters: `country`, `year`, `age`, and `position` If none of these parameters are given it should raise a `ValueError`.
The `search` method should return an iterator that contains all the records from the csv file *that match the given parameters* as Player objects.

It may make things easier to create a base iterator class for returning all records and then have a child class inherit from that for handling filtering search results.
