import os
import sys
import unittest
import itertools
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ppictx

fh = 'toy/data-raw/TOY-HIPPIE.mitab'
fp = 'toy/data-raw/TOY-PUBTATOR.gz'
fc = 'toy/data-raw/TOY-CELLOSAURUS.txt'