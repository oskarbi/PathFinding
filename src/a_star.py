"""
Implementation of A* search algorithm.
"""
import sys
import math

def dist_between(current, neighbor):
    return get_distance(current, neighbor)

def reconstruct_path(came_from, start, goal):
    """Build the list of nodes composing the path."""
    node = goal
    path = []
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(node)
    path.reverse()
    return path

def min_node(openset, f_score):
    min_weight = sys.maxint
    min_weight_node = None
    for node in openset:
        if f_score[node] < min_weight:
            min_weight = f_score[node]
            min_weight_node = node
    return min_weight_node

def heuristic_cost_estimate(start, goal):
    return get_distance(start, goal)

def get_distance(u, v):
    """Return the euclidean distance between two nodes."""
    return math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

def a_star(graph, start, goal):
    """Implementation of A* algorithm."""
    closedset = []
    openset = [start]
    came_from = {}

    g_score = {}
    f_score = {}
    g_score[start] = 0 # Cost from start along best known path.
    # Estimated total cost from start to goal through y.
    f_score[start] = g_score[start] + heuristic_cost_estimate(start, goal)

    while openset:
        current = min_node(openset, f_score)
        if current == goal:
            final_path = reconstruct_path(came_from, start, goal)
            return final_path, g_score[goal]

        openset.remove(current)
        closedset.append(current)
        for neighbor in graph[current]["neighbors"]:
            if neighbor in closedset:
                continue
            tentative_g_score = (g_score[current] +
                                 dist_between(current, neighbor))

            if not neighbor in openset or tentative_g_score < g_score[neighbor]:
                if not neighbor in openset:
                    openset.append(neighbor)
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = (g_score[neighbor] +
                                     heuristic_cost_estimate(neighbor, goal))

    raise Exception("Path not found")
