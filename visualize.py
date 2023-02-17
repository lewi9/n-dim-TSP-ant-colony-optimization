import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pointsList = [pd.read_csv(f"points{i}.txt", sep='\t', names=["distance","cost"]) for i in range(1,9)]
paretoFrontList = [pd.read_csv(f"paretoFront{i}.txt", sep='\t', names=["distance","cost"]) for i in range(1,9)]

points = pd.concat(pointsList)
paretoFront = pd.concat(paretoFrontList, ignore_index = True)

paretoFrontPlot = pd.DataFrame(columns = ["distance", "cost"])
                               
for index, row in paretoFront.iterrows():
    flag = 1
    for index2, row2 in paretoFront.iterrows():
        if row["distance"] > row2["distance"] and row["cost"] > row2["cost"]:
            flag = 0
    if flag == 1:
        dictionary = {"distance" : [row.values[0]], "cost" : [row.values[1]]}
        df = pd.DataFrame(dictionary)
        paretoFrontPlot = pd.concat([df,paretoFrontPlot])
print(paretoFrontPlot)
paretoFrontPlot = paretoFrontPlot.drop_duplicates()
points = points.drop_duplicates()

fig,ax = plt.subplots(1,1)
ax.scatter(x = points["distance"], y = points["cost"], c = "blue", alpha = 0.1)
ax.scatter(x = paretoFrontPlot["distance"], y = paretoFrontPlot["cost"], c = "red", s = 100, alpha = 0.3)
ax.set_xlabel("Distance")
ax.set_ylabel("Cost")
ax.set_title("Pareto Front visualizations 3-10 and sample of solutions(createPoints3 - for all runs 47-cities)")
ax.axis('square')
plt.show()
