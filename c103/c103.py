import pandas as pd
import plotly.express as px

df = pd.read_csv('data1.csv')
fig = px.scatter_geo(df, locations="country", size="cases")
fig.show()