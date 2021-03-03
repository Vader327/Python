import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as pf

"""count = []
sums=[]

for i in range(0, 100):
  a = random.randint(1, 6)
  b = random.randint(1, 6)
  sums.append(a+b)
  count.append(i)

fig = px.bar(x=sums, y=count)
fig.show()
"""

with open('data1.csv') as file:
  df = pd.read_csv(file)
  fig = pf.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=True)
  fig.show()