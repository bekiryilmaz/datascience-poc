#author: Bekir Yılmaz
#csv reader with pandas example
#06.02.2021
import os;
import csv;
import time;
import _datetime;
import math;
from array import *;
import random;
import pandas as pd;

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_dataset(datasetPath):
    path=os.path.join(__location__, datasetPath);
    _dataset=pd.read_csv(path, sep=';',encoding='utf-8');
    print(_dataset.columns);
    print(_dataset);
    return _dataset;    

def main():
    read_dataset("datasets/bank/bank-full.csv");

if __name__ == "__main__":
    main();