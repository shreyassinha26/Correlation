import csv
import pandas as pd
import plotly.express as px
import numpy as np
file1=pd.read_csv("txt/WeekCoffeeSleep.csv")
fig1=px.scatter(file1 , x="Coffee in ml" , y="sleep in hours")
file2=pd.read_csv("txt/RollMarksDays.csv")
fig2=px.scatter(file2 , x="Marks In Percentage" , y="Days Present")
fig1.show()
fig2.show()
def getDataSource(filepath , head1 , head2):
    x=[]
    y=[]
    with open(filepath) as f:
        reader=csv.DictReader(f)
        for i in reader:
            x.append(float(i[head1]))
            y.append(float(i[head2]))
    return {'x':x , 'y':y}
def correlation(dataset):
    correlation=np.corrcoef(dataset['x'] , dataset['y'])
    return correlation[0,1]
def setup1():
    dataset=getDataSource("txt/WeekCoffeeSleep.csv" , "Coffee in ml" , "sleep in hours")
    correlation1=correlation(dataset)
    print(correlation1)
def setup2():
    dataset=getDataSource("txt/RollMarksDays.csv" , "Marks In Percentage" , "Days Present")
    correlation2=correlation(dataset)
    print(correlation2)
setup1()
setup2()