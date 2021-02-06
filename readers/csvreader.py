#author: Bekir Yılmaz
#vanilla csv reader example
#06.02.2021
import os;
import csv;
import time;
import _datetime;
import math;
from array import *;
import random;
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_dataset(datasetPath):
    _dataset=[]
    with open(os.path.join(__location__, datasetPath),newline='') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=';', quotechar='|')
        index=0;
        for row in csvreader:
            print(row[0]);
    return _dataset;

def main():
    read_dataset("datasets/bank/bank-full.csv");

if __name__ == "__main__":
    main();