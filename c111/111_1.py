import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

print("Standard deviation of Population: ", statistics.stdev(data))
print("Mean of Population: ", statistics.mean(data))
print("\n")
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)

print("Mean of Sampling Distribution :", sample_mean)
print("Standard deviation of sampling distribution: ", statistics.stdev(mean_list))

fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
#fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 1], mode="lines", name="MEAN"))
fig.show()