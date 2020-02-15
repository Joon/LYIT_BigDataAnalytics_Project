#!/usr/bin/python

import sys
import pandas as pd

if (len(sys.argv) != 3):
    print("This script requires two parameters: a " + \
        "file path to a csv file to read, and another file " + \
        "path to a json to save as a parameter")
    sys.exit(1)

print("Reading data from {}".format(sys.argv[1]))
data = pd.read_csv(sys.argv[1]) 
print("Data has been read from CSV")
print("Data head:")
print(data.head())

print("Writing data to {}".format(sys.argv[2]))
data.to_json(sys.argv[2], orient='records')