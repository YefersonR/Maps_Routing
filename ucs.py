# https://stackoverflow.com/questions/43354715/uniform-cost-search-in-python
# https://plainenglish.io/blog/uniform-cost-search-ucs-algorithm-in-python-ec3ee03fca9f
# https://python.plainenglish.io/graph-data-structure-theory-and-python-implementation-ee8c9795eae7

from Mapa import (
    GetNodesChildren,
    GetWays,
    ways,
    Graph
)
from Front import draw_solution
import heapq #https://docs.python.org/3/library/heapq.html
def UCS(initialNode, goalNode, adjacencyList):
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
            draw_solution(initialNode,goalNode,solution)
            print("Se ha encontrado la ruta mas corta a su destino")
            # print(solution)

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
shorterPath = UCS((18.4870666,-69.8769768),(18.4819294, -69.8799627), g.getAdyacencia())


# (18.4873418,-69.8836541),(18.4869884,-69.8891887)
# (18.4857774,-69.8789543),(18.4870666,-69.8769768)
# (18.4961680,-69.8886738),(18.4857774,-69.8789543)
# (18.4961680,-69.8886738), (18.4759391, -69.9087016)
# (18.4870666,-69.8769768),(18.4819294, -69.8799627)

