class Node:
    def __init__(self, edges):
        self.edges = edges


class Edge:
    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost


def dijkstra(nodes):
    distances = [float('inf')] * len(nodes)
    distances[0] = 0

    rest_node_indices = [i for i in range(len(nodes))]

    while len(rest_node_indices) > 0:
        min_node_index = min(rest_node_indices, key=lambda i: distances[i])

        source_index = rest_node_indices.pop(rest_node_indices.index(min_node_index))
        for edge in nodes[source_index].edges:
            if distances[edge.destination] > distances[source_index] + edge.cost:
                distances[edge.destination] = distances[source_index] + edge.cost

    return distances


nodes = [
    Node([Edge(1, 4), Edge(2, 3)]),
    Node([Edge(2, 1), Edge(3, 1), Edge(4, 5)]),
    Node([Edge(5, 2)]),
    Node([Edge(4, 3)]),
    Node([Edge(6, 2)]),
    Node([Edge(4, 1), Edge(6, 4)]),
    Node([]),
]

print(dijkstra(nodes))

