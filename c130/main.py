import pandas as pd
import csv

df = pd.read_csv('data.csv')

req_headers = ['name',	'light_years_from_earth', 'planet_mass', 'stellar_magnitude', 'discovery_date', 'planet_type', 'planet_radius',	'orbital_radius',	'orbital_period',	'eccentricity', 'pl_facility']
all_headers = list(df.columns.values)

val_to_change = 'pl_hostname'
val = 'Planet Hostname'

"""
for index, h in enumerate(all_headers):
  if h == val_to_change:
    all_headers[index] = val
    df.columns = all_headers
"""


for index, h in enumerate(all_headers):
  if index > 12:
    df.rename(columns={h: h.upper()}, inplace=True)


#df.rename(columns={'pl_hostname': ""}, inplace=True)

"""
for h in all_headers:
  if h not in req_headers:
    del df[h]
"""

#print(df.columns.values)

#print(df.shape)

df.to_csv('final.csv')
