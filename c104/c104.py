from collections import Counter
import csv

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


n = len(new_data)
data = Counter(new_data)
get_mode = dict(data)

mode = []
modeOcc=[]

mode1 = []
mode1Occ=[]

mode2 = []
mode2Occ=[]

for a,v in get_mode.items():
    a= float(a)
    if 50< a <60:
        if v == max(list(data.values())):
            mode.append(a)
            modeOcc.append(v)
    elif 60< a <70:
        if v == max(list(data.values())):
            mode1.append(a)
            mode1Occ.append(v)
    elif 70< a <75:
        if v == max(list(data.values())):
            mode2.append(a)
            mode2Occ.append(v)

new_arr_1 = mode + mode1 + mode2
total = sum(new_arr_1)
n = len(new_arr_1)
print(total / n)
