from sys import maxsize
from itertools import permutations
import numpy as np
V = 10
 
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        if current_pathweight < min_path:
            previousPath = min_path
        min_path = min(min_path, current_pathweight)

    print(previousPath)
    return min_path
 
 
# Driver Code
if __name__ == "__main__":
    mainPath = "cities-10ns-"
    distancePath = mainPath + "distance.txt"
    #costPath = mainPath + "cost.txt"
    distance = np.genfromtxt(distancePath, delimiter="\t")
    #cost = np.genfromtxt(costPath, delimiter="\t")
    ## matrix representation of graph
    graph = distance.tolist()
    s = 0
    print(travellingSalesmanProblem(graph, s))
