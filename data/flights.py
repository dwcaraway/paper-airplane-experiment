"""
Flight performance (distance for paper airplane experiment)
"""

import pandas

from os.path import dirname, join

flights = pandas.read_csv(join(dirname(__file__), 'flights.csv'))
