import csv
import numpy as np

def dataSource(data_path):
    coffeeInMl=[]
    sleep=[]

    with open(data_path) as f:
        csv_reader=csv.DictReader(f)

        for row in csv_reader:
            coffeeInMl.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x":coffeeInMl,"y":sleep}

def findcorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"])
    print("Correlation between coffee in ml and hours of sleep is ",correlation[0,1])
    
path="coffee.csv"
data=dataSource(path)
findcorrelation(data)
