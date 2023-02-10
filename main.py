
#traveling saleman - symetric

import numpy as np

class Ant:
    def __init__(self, startCity):
        self.startCity = startCity
        self.tabooList = [startCity,]
        self.currentCity = startCity

# Paths to files with matrix: distance and cost    
mainPath = "cities-5-"
distancePath = mainPath + "distance.txt"
costPath = mainPath + "cost.txt"

# Parameters of algorithm
maxCycle = 500

antsInCity = 10
alpha = pheromoneWeight = 1
beta = cityVisibility = 1
vaporizeFactor = 0.2
Q = newPheromonFactor = 1
# Read data from files
distance = np.genfromtxt(distancePath, delimiter="\t")
cost = np.genfromtxt(costPath, delimiter="\t")

print("Distance matrix:")
print(distance)
print("\nCost matrix:")
print(cost)

# Init variables  
distanceCopy = distance
distanceMax = np.max(distance)
distance = distance/np.max(distance)
cost = cost/np.max(cost)
cities = cost.shape[0]

mostEffectivePath = np.max(distance) * cities
shortestPath = []
# Build pheromone matrix with initial value
pheromone = np.ones((cities, cities)) * abs(np.random.normal(0,1,1))

ants = []

# Algorithm
for k in range(maxCycle):
    if k % 50 == 0:
        print(f"iteration: {k} Shortest path: {mostEffectivePath*distanceMax}")
        print(pheromone)

    #create ants
    for i in range(cities):
        for j in range(antsInCity):
            ants.append(Ant(i))

    #travel through the cities
    for i in range(cities-1):
        for ant in ants:
            avalaibleCities = [x for x in np.arange(cities) if x not in ant.tabooList]
            sumTotal = np.sum( pheromone[ant.currentCity][avalaibleCities] ** alpha * ( 1/distance[ant.currentCity][avalaibleCities] ** beta ) )
            probabilityVector = pheromone[ant.currentCity][avalaibleCities] ** alpha * ( 1/distance[ant.currentCity][avalaibleCities] ** beta ) / sumTotal
            destinationCity = int(np.random.choice(avalaibleCities, 1, p=probabilityVector))
            ant.currentCity = destinationCity
            ant.tabooList.append(destinationCity)

    #check that all roads are the same and add pheromone
    flagSame = 1
    pattern = ants[0].tabooList
    patternReverse = pattern.reverse()
    anotherPath = 0
    for ant in ants:
        path = 0

        #check shortest path
        for i in range(cities):
            index = i-1
            path += distance[ant.tabooList[index]][ant.tabooList[i]]
        if path < mostEffectivePath:
            mostEffectivePath = path
            shortestPath = ant.tabooList

        #add pheromone
        for i in range(cities):
            index = i-1
            pheromone[ant.tabooList[i]][ant.tabooList[index]] *= (1-vaporizeFactor)
            pheromone[ant.tabooList[i]][ant.tabooList[index]] += Q/path

        #check path are the same
        rolled = 0
        for i in range(cities):
            if pattern == list(np.roll(ant.tabooList,i)):
                rolled = 1
                break
        if rolled != 1:
            for i in range(cities):
                if patternReverse == list(np.roll(ant.tabooList,i)):
                    rolled = 1
        if rolled == 0:
            flagSame = 0
            anotherPath += 1

    #stop condition
    if flagSame == 1:
        break

    triu = np.triu(pheromone).T
    tril = np.tril(pheromone).T
    pheromone += triu + tril
    A = np.ones((cities, cities))
    A -= np.eye(cities)
    pheromone *= A
        
    ants.clear()

print(f"Shortest path: {shortestPath}\n")      
print(f"Size of shortest path: {mostEffectivePath*np.max(distanceCopy)}\n") 
