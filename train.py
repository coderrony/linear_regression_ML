
import pandas as pd
import math
import json

data_set = r"C:\Users\ronyd\OneDrive\Desktop\phitronPY\module\oop\34_linear_regression\Sal_vs_Exp.csv"

data = pd.read_csv(data_set)
x = data[data.columns[0]]
y = data[data.columns[1]]


x_mean = data[data.columns[0]].mean()
y_mean = data[data.columns[1]].mean()


upper = 0
lower = 0
for index in range(len(x)):
    upper += (x[index] - x_mean) * (y[index] - y_mean)
    lower += math.pow(x[index] - x_mean, 2)

m = upper / lower
c = y_mean - (m*x_mean)

trained_data = {}
trained_data['m'] = m
trained_data['c'] = c
trained_data['y_mean'] = y_mean

with open("module/oop/34_linear_regression/trained_data.txt", 'w') as fill:
    fill.write(json.dumps(trained_data))

fill.close()

# print(x, y)
