import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy 

lowerLimitPoints = 1
upperLimitPoints = 10 + 1

lowerLimitPareto = 11
upperLimitPareto = 11 + 1

file = "figures/Figure_12.png"
#pieChart = "figures/Pie_11.png"

title = "Pareto Front 47-cities-ns (250 iterations, 100 ants) vs all solutions of 10 simulations"

cols = ["distance","cost"]

pointsList = [pd.read_csv(f"results/points{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPoints,upperLimitPoints)]
paretoFrontList = [pd.read_csv(f"results/paretoFront{i}.txt", sep='\t', names=cols) for i in range(lowerLimitPareto,upperLimitPareto)]

for i in range(len(paretoFrontList)):
    paretoFrontList[i]["category"] = i+lowerLimitPareto

points = pd.concat(pointsList)
paretoFront = pd.concat(paretoFrontList, ignore_index = True)

colsExtended = copy.copy(cols)
colsExtended.append("category")

paretoFrontPlot = pd.DataFrame(columns=colsExtended)
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
        dictionary = {cols[0] : [row.values[0]], cols[1] : [row.values[1]], "category" : [row.values[2]]}
        df = pd.DataFrame(dictionary)
        paretoFrontPlot = pd.concat([df,paretoFrontPlot])


points = points.drop_duplicates()

fig,ax = plt.subplots(1,1, figsize=(10,10))
ax.scatter(x = points[cols[0]], y = points[cols[1]], c = "blue", alpha = 0.1)
ax.scatter(x = paretoFrontPlot[cols[0]], y = paretoFrontPlot[cols[1]], c = "red", s = 100, alpha = 0.3)
ax.set_xlabel(cols[0])
ax.set_ylabel(cols[1])
ax.set_title(title)
ax.axis('square')
plt.savefig(file)
plt.close()

fig,ax = plt.subplots(1,1,figsize=(10,10))
ax.pie(np.array(paretoFrontPlot["category"].value_counts().values), labels = paretoFrontPlot["category"].value_counts().index)
ax.set_title("Contribution of the simulation to the final result - 47-cities-ns")
#plt.savefig(pieChart)
plt.close()
