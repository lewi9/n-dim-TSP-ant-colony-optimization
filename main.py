
## traveling saleman

import numpy as np

class Ant:
    def __init__(self, startCity):
        self.startCity = startCity
        self.tabooList = [startCity,]
        self.currentCity = startCity

## Paths to files with matrix: distance and cost    
mainDir = "cities-10ns-"
distanceDir = mainDir + "distance.txt"
costDir = mainDir + "cost.txt"

## Parameters of algorithm
maxCycle = 500

antsInCity = 10

alpha = pheromoneWeight = 1
beta = cityVisibility = 2
q = exploitationOrExploration = 0.6
vaporizeFactor = 0.7
pheromoneZero = 0.2

## Read data from files
distance = np.genfromtxt(distanceDir, delimiter="\t")
cost = np.genfromtxt(costDir, delimiter="\t")

print("Distance matrix:")
print(distance)
print("\nCost matrix:")
print(cost)

## Init variables  
distanceCopy = distance
distanceMax = np.max(distance)
distance = distance/np.max(distance)
cost = cost/np.max(cost)
cities = cost.shape[0]

antsOnPath = 0

mostEffectivePath = np.max(distance) * cities
shortestPath = list(np.arange(cities))

## Build pheromone matrix with initial value
pheromone = np.ones((cities, cities)) * pheromoneZero

ants = []

## Algorithm
for k in range(maxCycle):

    localPheromone = np.copy(pheromone)    
    ## create ants
    for i in range(cities):
        for j in range(antsInCity):
            ants.append(Ant(i))

    ## travel through the cities
    for i in range(cities-1):
        for ant in ants:
            avalaibleCities = [x for x in np.arange(cities) if x not in ant.tabooList]
            sumTotal = np.sum( localPheromone[ant.currentCity][avalaibleCities] ** alpha * ( 1/distance[ant.currentCity][avalaibleCities] ** beta ) )
            probabilityVector = localPheromone[ant.currentCity][avalaibleCities] ** alpha * ( 1/distance[ant.currentCity][avalaibleCities] ** beta ) / sumTotal
            if np.random.sample() < q:
                destinationCity = int(np.random.choice(avalaibleCities, 1, p=probabilityVector))
            else:
                destinationCity = avalaibleCities[list(probabilityVector).index(np.max(probabilityVector))]
            ant.currentCity = destinationCity
            ant.tabooList.append(destinationCity)
            localPheromone[ant.tabooList[-2]][ant.tabooList[-1]] = localPheromone[ant.tabooList[-2]][ant.tabooList[-1]]*(1-vaporizeFactor) + vaporizeFactor*pheromoneZero

    ## check that all roads are the same and add pheromone
    for ant in ants:
        path = 0

        ## check shortest path
        for i in range(cities):
            index = i-1
            path += distance[ant.tabooList[index]][ant.tabooList[i]]
        if path <= mostEffectivePath:
            mostEffectivePath = path
            shortestPath = ant.tabooList

        ## add pheromone
    for i in range(cities):
        index = i-1
        pheromone[shortestPath[index]][shortestPath[i]] = pheromone[shortestPath[index]][shortestPath[i]]*(1-vaporizeFactor) + vaporizeFactor/mostEffectivePath
    
    ants.clear()

print(pheromone)
print(f"Shortest path: {shortestPath}\n")      
print(f"Size of shortest path: {int(mostEffectivePath*np.max(distanceCopy))}\n") 
