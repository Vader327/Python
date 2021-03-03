import csv
import plotly.express as px
import pandas as pd

file = open('class2.csv', newline="")
reader = csv.reader(file)
file_data = list(reader)

file_data.pop(0)
data = []
for x in range(len(file_data)):
  data.append(float(file_data[x][1]))

sum = 0
n = len(data)
for x in data:
  sum += x

mean = sum / n

fig = px.scatter(pd.read_csv('class2.csv'), x="Student Number", y="Marks")
fig.update_layout(shapes=[dict(type="line", y0=mean, y1=mean, x0=0, x1=n)])
fig.update_yaxes(rangemode="tozero")
fig.show()