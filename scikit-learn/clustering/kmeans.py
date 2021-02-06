#author: Bekir Yılmaz
#scikit-learn kmeans clustering example
#06.02.2021
import pandas as pd;
from sklearn.cluster import KMeans;
import numpy as np;

def main():
    #data
    array=np.array([[1,2],[1,4],[4,9],[12,2]]);
    
    #do clustering 
    kmeans=KMeans(n_clusters=3).fit(array);
    
    #show clusters of all points
    print(kmeans.labels_);
    
    #predict new points
    prediction=kmeans.predict([[0,0],[13,4]]);
    print(prediction);

if __name__ == "__main__":
    main();