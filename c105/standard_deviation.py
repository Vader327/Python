import csv
import plotly.express as px
import pandas as pd
import math

with open('data.csv', newline="") as file:
  reader = csv.reader(file)
  file_data = list(reader)

file_data.pop(0)
data = []
for x in range(len(file_data)):
  data.append(float(file_data[x][0]))

sum = 0
n = len(data)
for x in data:
  sum += x
mean = sum / n

squared=[]
for i in data:
  squared.append((int(i)-mean)**2)

sqr_sum = 0
for i in squared:
  sqr_sum += i

std_dev = math.sqrt(sqr_sum /(n))
print(std_dev)
