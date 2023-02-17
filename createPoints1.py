from itertools import permutations
import numpy as np

V = 10


def createPoints(graph, graph2, s):

    points = []
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    next_permutation=permutations(vertex)
    iterator = 0
    for i in next_permutation:
        current_pathweight = np.zeros((2,1))
        k = s
        for j in i:
            current_pathweight[0] += graph[k][j]
            current_pathweight[1] += graph2[k][j]
            k = j
        current_pathweight[0] += graph[k][s]
        current_pathweight[1] += graph2[k][s]
        points.append(current_pathweight)
        
    return points
 
# Driver Code
if __name__ == "__main__":
    mainPath = "cities-10ns-"
    distancePath = mainPath + "distance.txt"
    costPath = mainPath + "cost.txt"
    delim = "\t"
    distance = np.genfromtxt(distancePath, delimiter=delim)
    #cost = np.genfromtxt(costPath, delimiter=delim)
    cost = np.genfromtxt(costPath, delimiter=delim)
    graph = distance.tolist()
    graph2 = cost.tolist()
    s = 0
    points = createPoints(graph, graph2, s)
    saveToFile = np.reshape(points, (len(points),2))
    np.savetxt("points.txt", saveToFile, delimiter='\t')
