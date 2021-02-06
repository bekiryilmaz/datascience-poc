#author: Bekir Yılmaz
#scikit-learn kmeans clustering example
#07.02.2021
import os;
import csv;
import time;
import _datetime;
import math;
import pandas as pd;
from sklearn.cluster import KMeans;
import numpy as np;

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_dataset(datasetPath):
    _dataset=[]
    with open(os.path.join(__location__, datasetPath),newline='') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar='|')
        index=0;
        for row in csvreader:
            if index>0:
                print(row[3]+" / "+row[6])
                _dataset.append([row[3],row[6]])
            index=index+1
    return _dataset;

def main():

    dataset=read_dataset("dataset/tripadvisor_review.csv");

    #data
    array=np.array([[1,2],[1,4],[4,9],[12,2]]);
    
    #do clustering 
    kmeans=KMeans(n_clusters=2).fit(dataset);
    
    #show clusters of all points
    print(kmeans.labels_);
    
    #predict new points
    prediction=kmeans.predict([[0,0],[13,4]]);
    print(prediction);

if __name__ == "__main__":
    main();