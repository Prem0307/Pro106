import csv
import numpy as np

def dataSource(data_path):
    sizeOftV=[]
    averageTimeSpent=[]

    with open(data_path) as f:
        csv_reader=csv.DictReader(f)

        for row in csv_reader:
            sizeOftV.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time"]))

    return {"x":sizeOftV,"y":averageTimeSpent}

def findcorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"])
    print("Correlation between size of tv and average time is ",correlation[0,1])
    
path="tv.csv"
data=dataSource(path)
findcorrelation(data)
