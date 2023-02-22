import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lowerLimitPoints = 1
upperLimitPoints = 10 + 1

lowerLimitPareto = 1
upperLimitPareto = 10 + 1

file = "figures/Figure_11.png"

title = "Pareto Front 47-cities-ns 10 simulations vs all solutions of 10 simulations"

cols = ["distance","cost"]

pointsList = [pd.read_csv(f"results/points{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPoints,upperLimitPoints)]
paretoFrontList = [pd.read_csv(f"results/paretoFront{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPareto,upperLimitPareto)]

points = pd.concat(pointsList)
paretoFront = pd.concat(paretoFrontList, ignore_index = True)

paretoFrontPlot = pd.DataFrame(columns=cols)
paretoFrontPlot = paretoFrontPlot.drop_duplicates()
             
for index, row in paretoFront.iterrows():
    flagAdd = 1
    for index2, row2 in paretoFront.iterrows():
        flagSecond = 0
        for colname in cols:
            if row[colname] > row2[colname]:
                flagSecond += 1
        if flagSecond == len(cols):
            flagAdd = 0
    if flagAdd == 1:
        dictionary = {cols[0] : [row.values[0]], cols[1] : [row.values[1]]}
        df = pd.DataFrame(dictionary)
        paretoFrontPlot = pd.concat([df,paretoFrontPlot])
print(paretoFrontPlot)

points = points.drop_duplicates()

fig,ax = plt.subplots(1,1, figsize=(10,10))
ax.scatter(x = points[cols[0]], y = points[cols[1]], c = "blue", alpha = 0.1)
ax.scatter(x = paretoFrontPlot[cols[0]], y = paretoFrontPlot[cols[1]], c = "red", s = 100, alpha = 0.3)
ax.set_xlabel(cols[0])
ax.set_ylabel(cols[1])
ax.set_title(title)
#ax.axis('square')
plt.savefig(file)
