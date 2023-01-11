import pandas as pd
import math
import json
import matplotlib.pyplot as plt

data_set = r"C:\Users\ronyd\OneDrive\Desktop\phitronPY\module\oop\34_linear_regression\Sal_vs_Exp.csv"

data = pd.read_csv(data_set)
x = data[data.columns[0]]
y = data[data.columns[1]]

x = x.truncate(4900, 4999)
y = y.truncate(4900, 4999)

with open("module/oop/34_linear_regression/trained_data.txt") as fill:
    data = fill.read()
    convert = json.loads(data)

m = convert['m']
c = convert['c']
y_mean = convert['y_mean']

y_predicted_list = []
r_upper = 0
r_lower = 0

for index in x:
    y_predicted = (m*x[index+4900]) + c
    y_predicted_list.append(y_predicted)
    r_upper += math.pow((y[index+4900] - y_predicted), 2)
    r_lower = math.pow((y[index+4900] - y_mean), 2)

# r_square = 1 - (r_upper/r_lower)
# print(r_square)


# plt.scatter(x, y, color='g')
# plt.plot(x, y_predicted_list, color='r')
# plt.show()


inp = int(input("enter year: "))
predicted = (m * inp) + c
print(predicted)
