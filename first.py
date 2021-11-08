import csv
import numpy as np 
import plotly.express as pd

with open("tv.csv") as f:
    df=csv.DictReader(f)
    fig=pd.scatter(df,x="Size of TV",y="\tAverage time")
    fig.show()



