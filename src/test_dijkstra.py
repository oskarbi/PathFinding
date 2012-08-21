import unittest
from dijkstra import dijkstra

class Test1TestCase(unittest.TestCase):

    def testOneNode(self):
        node_1 = (0, 0)

        graph = {
            node_1: {"neighbors": []}
            }
        path, distance = dijkstra(graph, node_1, node_1)

        self.assertEqual(path, [(0, 0)])
        self.assertEqual(distance, 0.0)

    def testTwoNodes(self):
        node_1 = (0, 0)
        node_2 = (0, 1)

        graph = {
            node_1: {"neighbors": [node_2]},
            node_2: {"neighbors": [node_1]}
            }
        path, distance = dijkstra(graph, node_1, node_2)

        self.assertEqual(path, [(0, 0), (0, 1)])
        self.assertEqual(distance, 1.0)

    def testThreeNodes(self):
        """Tres nodos equidistantes."""
        node_1 = (0, 0)
        node_2 = (0, 1)
        node_3 = (1, 0)

        graph = {
            node_1: {"neighbors": [node_2, node_3]},
            node_2: {"neighbors": [node_1, node_3]},
            node_3: {"neighbors": [node_1, node_2]}
            }
        path, distance = dijkstra(graph, node_1, node_2)

        self.assertEqual(path, [(0, 0), (0, 1)])
        self.assertEqual(distance, 1.0)

    def testThreeNodes2(self):
        """Tres nodos encadenados en linea recta."""
        node_1 = (0, 0)
        node_2 = (1, 0)
        node_3 = (2, 0)

        graph = {
            node_1: {"neighbors": [node_2]},
            node_2: {"neighbors": [node_3]},
            node_3: {"neighbors": [node_2]}
            }
        path, distance = dijkstra(graph, node_1, node_3)

        self.assertEqual(path, [(0, 0), (1, 0), (2, 0)])
        self.assertEqual(distance, 2.0)

    def testFourNodes1(self):
        """Grafo de 4 nodos, todos interconectados."""
        node_1 = (0, 0)
        node_2 = (1, 0)
        node_3 = (0, 1)
        node_4 = (1, 1)

        graph = {
            node_1: {"neighbors": [node_2, node_3, node_4]},
            node_2: {"neighbors": [node_1, node_3, node_4]},
            node_3: {"neighbors": [node_1, node_2, node_4]},
            node_4: {"neighbors": [node_2, node_3, node_1]}
            }
        path, distance = dijkstra(graph, node_1, node_4)

        self.assertEqual(path, [(0, 0), (1, 1)])
        self.assertEqual(round(distance, 5), 1.41421)

    def testFourNodes2(self):
        """Grafo de 4 nodos, interconectados como un cuadrado."""
        node_1 = (0, 0)
        node_2 = (1, 0)
        node_3 = (0, 1)
        node_4 = (1, 1)

        graph = {
            node_1: {"neighbors": [node_2, node_3]},
            node_2: {"neighbors": [node_1, node_4]},
            node_3: {"neighbors": [node_1, node_4]},
            node_4: {"neighbors": [node_2, node_3]}
            }
        path, distance = dijkstra(graph, node_1, node_4)

        self.assertEqual(path, [(0, 0), (1, 0), (1, 1)])
        self.assertEqual(distance, 2.0)

    def testSix(self):
        """Ejemplo copiado de la Wikipedia."""
        node_1 = (1, 0)
        node_2 = (0, 1)
        node_3 = (2, 1)
        node_4 = (2, 3)
        node_5 = (4, 2)
        node_6 = (3, 0)

        graph = {node_1: {"neighbors": [node_2, node_3, node_6]},
                 node_2: {"neighbors": [node_1, node_3, node_4]},
                 node_3: {"neighbors": [node_1, node_2, node_4, node_6]},
                 node_4: {"neighbors": [node_2, node_3, node_5]},
                 node_5: {"neighbors": [node_4, node_6]},
                 node_6: {"neighbors": [node_1, node_3, node_5]}
                 }
        path, distance = dijkstra(graph, node_1, node_5)

        self.assertEqual(path, [(1, 0), (3, 0), (4, 2)])
        self.assertEqual(round(distance, 5), 4.23607)


if __name__ == "__main__":
    unittest.main()
