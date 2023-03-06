from Mapa import (
    GetNodesChildren,
    GetWays,
    ways,
    Graph
)
import heapq
def prueba_UCS(initialNode, goalNode, adjacencyList):
    FrontierCost = []

    frontier = []
    explored = []
    path = dict()
    path[initialNode] = initialNode
    
    heapq.heappush(FrontierCost, (initialNode, 0))
    frontier.append(initialNode)

    cost = dict()

    cost[initialNode] = 0

    while len(FrontierCost) > 0:
        state = heapq.heappop(FrontierCost)
        explored.append(state[0])

        if(state[0] == goalNode or state[0]not in adjacencyList):

            solution = []
            n = state[0]

            while path[n] != n:
                solution.append(n)
                n = path[n]

            solution.append(initialNode)
            solution.reverse()
            print("Ha llegado a su destino")
            print(solution)

            break

        for (neighbor, costNeighbor) in adjacencyList[state[0]]:

            if (neighbor not in frontier and neighbor not in explored):
                cost[neighbor]= cost[state[0]] + costNeighbor
                heapq.heappush(FrontierCost, (neighbor, costNeighbor))
                path[neighbor] = state[0]
                frontier.append(neighbor)

            elif cost[neighbor] > cost[state[0]] + costNeighbor:
                cost[neighbor] = cost[state[0]] + costNeighbor
                path[neighbor] = state[0]
    return


g = Graph(ways)
print(prueba_UCS((18.4870666,-69.8769768),(18.4961680,-69.8886738), g.getAdyacencia()))


# (18.4857774,-69.8789543), (18.4850415,-69.8813206)
# (18.4940667, -69.8894379), (18.4857774,-69.8789543)
# (18.4961680,-69.8886738), (18.4947003,-69.8953688)
# (18.4870666,-69.8769768),(18.4961680,-69.8886738)
# 
