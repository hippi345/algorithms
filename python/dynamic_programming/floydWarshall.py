# Floyd Warshall Algorithm in python

# The number of vertices
nV = 4

INF = 99999999

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]]
# DP method call for solution
floyd_warshall(G)

'''
Floyd-Warshall is just Bellman-Ford but for every vertex in the graph over all edges.
Core algorithm is the same as Bellman-Ford -> distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]).
Runtime is O(N^3).

Notes on matrix and graph representation and the underlying algorithm:
The dimensions of the matrix, which represents the graph is nxn where n is the number of vertices in the graph.
Each cell [i][j] is the distance from the ith vertex to the jth vertex. Lack of a path will keep the value of that as infinity.
This is accurate as infinity is the distance between two vertices with no discernable path to traverse between them.
'''