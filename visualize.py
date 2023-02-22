import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lowerLimitPoints = 0
upperLimitPoints = 0 + 1

lowerLimitPareto = 0
upperLimitPareto = 0 + 1

file = "figures/Figure_111.png"

title = "Pareto Front 10-cities-ns vs all solutions of that problem"

cols = ["distance","cost"]

pointsList = [pd.read_csv(f"results/points{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPoints,upperLimitPoints)]
paretoFrontList = [pd.read_csv(f"results/paretoFront{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPareto,upperLimitPareto)]

points = pd.concat(pointsList)
paretoFront = pd.concat(paretoFrontList, ignore_index = True)

paretoFrontPlot = pd.DataFrame(columns=cols)
paretoFrontPlot = paretoFrontPlot.drop_duplicates()
             
for index, row in paretoFront.iterrows():
    flag = 0
    for index2, row2 in paretoFront.iterrows():
        for colname in cols:
            if row[colname] > row2[colname]:
                flag += 1
    if flag != len(cols):
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
