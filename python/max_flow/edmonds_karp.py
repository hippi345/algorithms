# Maximum flow implementation of a network of connections with the help of BFS,
# Rendition of the Wikipedia solution at https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
"""
Credit to https://github.com/volkansonmez/Algorithms-and-Data-Structures-2/blob/master/Max_Flow_and_Max_BP_Matching_in_Graphs.ipynb
"""
import numpy as np


class Graph:

    def __init__(self, graph):
        self.graph = np.copy(graph)  # graph with max flow capacities from each vertex

    # Returns tne maximum flow from s to t in the given graph
    def max_flow_edmonds_karp(self, source, sink):
        N, D = self.graph.shape
        # initialize a parent array
        parent = -np.ones(D, dtype=int)

        # augment the flow while there is path from source to sink,
        # for each path between source and sink, the parent array is continually updated with BFS
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity (or max flow) of the edges along the path filled by BFS.
            min_path_flow = np.inf
            t = sink  # initialize target as sink

            # from sink to source traverse all parents and find the min flow between all vertices
            while (t != source):
                min_path_flow = min(min_path_flow, self.graph[parent[t]][t])
                t = parent[t]

                # update residual capacities of the edges and reverse edges along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= min_path_flow
                self.graph[v][u] += min_path_flow
                v = parent[v]
                # the residual network is updated

        # extract the optimized network flow from the optimized residual network
        updated_network = self.draw_the_updated_network_flow()

        print('network of the optimized graph with the max flow:')
        print(updated_network)  # to view the network in equilibrium (when in is equal to out)
        # assert that total amount dispatched from source is equal to the total amount received at target
        assert (np.sum(updated_network[source, :]) == np.sum(updated_network[:, sink]))
        # the max flow into the system at equilibrium is ready to output
        return np.sum(updated_network[source, :])  # sum of all inputs from the source vertex into the network

    # simple BFS checks if there is a path from s to t, and returns T or F of a changing graph with a parent array
    def BFS(self, source, target, parent):
        # parent array is an additional feature that will keep being updated for each time BFS is run

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = [source]

        # Mark the source node as visited and enqueue it
        visited[source] = True

        # Standard BFS Loop
        while len(queue) > 0:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u that have not been visited,
            # mark them visited and then enqueue
            for i in range(len(self.graph[u])):
                # check if the index is not visited and graph has a value at [u][i] that is being updated
                if visited[i] == False and self.graph[u][i] > 0:
                    # append the vertex to the queue, mark it as True, update parent for all connecting vertices
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u

                    # if we reached sink in BFS starting from source, then return true, else false
        # equilibrium is reached when source vertex output == target vertex input
        # when self.graph[target vertex][vertex_at_i_index] == 0 so that visited[t] returns FALSE
        return visited[target]  # returns True if visited[t] else it returns False (flow conservation)

    def draw_the_updated_network_flow(self):
        # transpose of the final residual graph would be the graph with the optimized max flow
        n, d = self.graph.shape
        updated_graph = np.zeros([d, n], dtype=float)
        for i in range(n):
            for j in range(d):
                updated_graph[j][i] = self.graph[i][j]
        return updated_graph


test_graph = np.array([[0, 16, 13, 0, 0, 0],
                       [0, 0, 10, 12, 0, 0],
                       [0, 4, 0, 0, 14, 0],
                       [0, 0, 9, 0, 0, 20],
                       [0, 0, 0, 7, 0, 4],
                       [0, 0, 0, 0, 0, 0]], dtype=float)

g = Graph(test_graph)
print('max flow: ', g.max_flow_edmonds_karp(0, 5), '\n')
print('original graph:', '\n', np.array(test_graph))  # view the original flow of the network
# to view how the graph has been shaped to its final form


# The above implementation of Ford Fulkerson Algorithm is called Edmonds-Karp Algorithm.
# The idea of Edmonds-Karp is to use BFS in Ford Fulkerson implementation as BFS which always picks a path
# with minimum number of edges. When BFS is used, the worst case time complexity can be reduced to O(VE2).