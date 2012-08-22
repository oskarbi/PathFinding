PathFinding
===========

Implementations of path finding algorithms.

Pseudocode for the implemented algorithms (from Wikipedia):

Dijkstra pseudocode
-------------------
::

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

A* pseudocode
-------------
::

    function A*(start, goal)
         closedset := the empty set     // The set of nodes already evaluated.
         openset := {start}             // The set of tentative nodes to be evaluated, initially containing the start node
         came_from := the empty map     // The map of navigated nodes.

         g_score[start] := 0            // Cost from start along best known path.
         // Estimated total cost from start to goal through y.
         f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)

         while openset is not empty
             current := the node in openset having the lowest f_score[] value
             if current = goal
                 return reconstruct_path(came_from, goal)

             remove current from openset
             add current to closedset
             for each neighbor in neighbor_nodes(current)
                 if neighbor in closedset
                     continue
                 tentative_g_score := g_score[current] + dist_between(current,neighbor)

                 if neighbor not in openset or tentative_g_score < g_score[neighbor]
                     if neighbor not in openset
                         add neighbor to openset
                     came_from[neighbor] := current
                     g_score[neighbor] := tentative_g_score
                     f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)

         return failure

     function reconstruct_path(came_from, current_node)
         if came_from[current_node] is set
             p := reconstruct_path(came_from, came_from[current_node])
             return (p + current_node)
         else
             return current_node
