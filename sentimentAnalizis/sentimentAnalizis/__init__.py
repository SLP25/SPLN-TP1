#!/usr/bin/env python3

'''
Name 

SYNOPSIS


DESCRIPTIONS

FILES:


'''

__version__ = "0.0.1"

from .datasetParsers.parse import parseDatasets
from .parser import analize

def init():
    parseDatasets('parsedDatasets','datasets')

def main():
    while True:
        analize()