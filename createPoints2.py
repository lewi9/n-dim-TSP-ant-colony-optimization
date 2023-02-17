import numpy as np

mainPath = "cities-47-"
distancePath = mainPath + "distance.txt"
costPath = mainPath + "cost.txt"
delim = " "
distance = np.genfromtxt(distancePath, delimiter=delim)
cost = np.genfromtxt(costPath, delimiter=delim).T

distanceCopy = distance
distanceMax = np.max(distance)
distance = distance/np.max(distance)

costCopy = cost
costMax = np.max(cost)
cost = cost/np.max(cost)

matrices = [distance, cost]
matricesNumber = 2

cities = cost.shape[0]

maxes = [distanceMax, costMax]
paretoFront = []

maxCycles = 500000
q = exploitationOrExploration = 0.95

factor1 = 0.3
factor2 = 0.4
points = []

for k in range(maxCycles+2):
    path = []
    tabooList = [np.random.randint(0,cities)]
    for i in range(cities-1):
        avalaibleCities = [x for x in np.arange(cities) if x not in tabooList]
        sumHeuristic = 0

        flag = 1
        for j in range(matricesNumber):
            if np.random.sample() < factor1:
                sumHeuristic += matrices[j][tabooList[-1]][avalaibleCities]
                flag = 0
        if flag == 1:
            for j in range(matricesNumber):
                sumHeuristic += matrices[j][tabooList[-1]][avalaibleCities]
                
        if k == 0:
             destinationCity = avalaibleCities[list(sumHeuristic).index(np.min(sumHeuristic))]
        elif k == maxCycles+1:
            destinationCity = avalaibleCities[list(sumHeuristic).index(np.max(sumHeuristic))]
        else:
            if np.random.sample() < factor2:
                sumHeuristic = np.sqrt(sumHeuristic)
            elif np.random.sample() < factor2:
                sumHeuristic = sumHeuristic**2
                
            sumHeuristic = 1/sumHeuristic
            sumTotal = np.sum( sumHeuristic )
            probabilityVector = sumHeuristic / sumTotal
            if np.random.sample() < q:
                destinationCity = int(np.random.choice(avalaibleCities, 1, p=probabilityVector))
            else:
                destinationCity = avalaibleCities[list(probabilityVector).index(np.max(probabilityVector))]
        tabooList.append(destinationCity)
    path = np.zeros((matricesNumber,1))
    for i in range(cities):
        index = i-1
        for j in range(matricesNumber):
            path[j] += matrices[j][tabooList[index]][tabooList[i]]
    points.append(path)
    if k%(maxCycles/100) == 0:
        print(f"{k} iters passed")
for i in range(len(points)):
    for j in range(matricesNumber):
        points[i][j] *= maxes[j]
saveToFile = np.reshape(points, (len(points),matricesNumber))
np.savetxt("points.txt", saveToFile, delimiter='\t')
