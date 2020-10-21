import heapq

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
    queue = []
    heapq.heappush(queue, (0, 0))

    while len(queue) > 0:
        _, source_index = heapq.heappop(queue)
        for edge in nodes[source_index].edges:
            distance_via_edge = distances[source_index] + edge.cost
            if distances[edge.destination] > distance_via_edge:
                distances[edge.destination] = distance_via_edge
                heapq.heappush(queue, (distance_via_edge, edge.destination))

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
