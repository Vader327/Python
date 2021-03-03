import plotly.express as px
import pandas as pd
import numpy as np
import csv


def getDataSource(data_path):
  iceCreamSales = []
  coldDrinkSales = []

  with open(data_path, 'r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for row in csv_reader:
      iceCreamSales.append(float(row["Coffee in ml"]))
      coldDrinkSales.append(float(row["sleep in hours"]))

    return {"x": iceCreamSales, "y": coldDrinkSales}

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"], datasource["y"])
  print("Correlation between Coffee in ml vs Sleep in hours: ", correlation[0, 1])

def setup():
  data_path = "data4.csv"
  datasource = getDataSource(data_path)
  findCorrelation(datasource)

setup()

#fig = px.scatter(pd.read_csv('data1.csv'), x="Coffee in ml", y="sleep in hours")
#fig.show()