class Edge:
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost


def bellman_ford(edges, num_nodes):
    distances = [float('inf') for i in range(num_nodes)]
    distances[0] = 0

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if distances[edge.destination] > distances[edge.source] + edge.cost:
                distances[edge.destination] = distances[edge.source] + edge.cost
                changed = True

    return distances

edges = [
    Edge(0, 1, 4),
    Edge(0, 2, 3),
    Edge(1, 2, 1),
    Edge(1, 3, 1),
    Edge(1, 4, 5),
    Edge(2, 5, 2),
    Edge(4, 6, 2),
    Edge(5, 4, 1),
    Edge(5, 6, 4),
]

print(bellman_ford(edges, 7))
