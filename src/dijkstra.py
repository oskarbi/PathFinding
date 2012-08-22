"""
Implementation of Dijkstra search algorithm.
"""
import sys
import math

def min_node(nodes):
    """Return the node with the minimun weight from the list."""
    min_weight = sys.maxint
    min_weight_node = None
    for n in nodes:
        if n[1] < min_weight:
            min_weight = n[1]
            min_weight_node = n[0]
    return min_weight_node, min_weight

def get_distance(u, v):
    """Return the euclidean distance between two nodes."""
    return math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

def dijkstra(graph, s, d):
    """Return the shortest path between two nodes in a graph and
    the distance between them.
    """
    distance = {}
    previous = {}
    for node in graph:
        distance[node] = sys.maxint
        previous[node] = None

    distance[s] = 0
    queue = [(s, distance[s])]

    while queue:
        u, u_distance = min_node(queue) # Priorize the shortest paths found
        if u == d:
            break # We've reached the destination

        queue.remove((u, u_distance))

        for v in graph[u]["neighbors"]:
            if distance[v] > u_distance + get_distance(u, v):
                distance[v] = u_distance + get_distance(u, v)
                previous[v] = u
                queue.append((v, distance[v]))

    # Build the list of nodes composing the path
    node = d
    path = []
    while node != s:
        path.append(node)
        node = previous[node]
    path.append(node)
    path.reverse()

    return path, distance[d]
