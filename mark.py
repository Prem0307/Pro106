import csv
import numpy as np

def dataSource(data_path):
    marks=[]
    daysPresent=[]

    with open(data_path) as f:
        csv_reader=csv.DictReader(f)

        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x":marks,"y":daysPresent}

def findcorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"])
    print("Correlation between marks and days present is ",correlation[0,1])
    
path="marks.csv"
data=dataSource(path)
findcorrelation(data)
