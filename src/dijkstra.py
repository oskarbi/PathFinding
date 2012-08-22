"""
Dijkstra algorithm pseudocode (from Wikipedia):

function Dijkstra(Graph, source):
    for each vertex v in Graph:                                // Initializations
        dist[v] := infinity ;                                  // Unknown distance function from source to v
        previous[v] := undefined ;                             // Previous node in optimal path from source

    dist[source] := 0 ;                                        // Distance from source to source
    Q := the set of all nodes in Graph ;                       // All nodes in the graph are unoptimized - thus are in Q

    while Q is not empty:                                      // The main loop
        u := vertex in Q with smallest distance in dist[] ;    // Start node in first case
        if dist[u] = infinity:
            break ;                                            // all remaining vertices are
                                                               // inaccessible from source

        remove u from Q ;
        for each neighbor v of u:                              // where v has not yet been removed from Q.
            alt := dist[u] + dist_between(u, v) ;
            if alt < dist[v]:                                  // Relax (u,v,a)
                dist[v] := alt ;
                previous[v] := u ;
                decrease-key v in Q;                           // Reorder v in the Queue
    return dist;
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
