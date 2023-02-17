import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

points = pd.read_csv("points.txt", sep='\t', names=["distance","cost"])
paretoFront = pd.read_csv("paretoFront.txt", sep='\t', names=["distance","cost"])

fig,ax = plt.subplots(1,1)
ax.scatter(x = points["distance"], y = points["cost"], c = "blue", alpha = 0.1)
ax.scatter(x = paretoFront["distance"], y = paretoFront["cost"], c = "red", s = 100, alpha = 0.3)
ax.set_xlabel("Distance")
ax.set_ylabel("Cost")
ax.set_title("Pareto Front (300 iters, 30 ants) and cloud of solutions (all - createPoints1)")
#ax.axis('square')
plt.show()
