import heapq

class Node:
    def __init__(self, edges):
        self.edges = edges


class Edge:
    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost


def astar(nodes, esimated_distances, goal):
    distances = [float('inf')] * len(nodes)
    distances[0] = 0
    queue = []
    heapq.heappush(queue, (0, [0]))

    while len(queue) > 0:
        _, route = heapq.heappop(queue)
        source_index = route[-1]

        if source_index == goal:
            return route

        for edge in nodes[source_index].edges:
            distance_via_edge = distances[source_index] + edge.cost
            if distances[edge.destination] > distance_via_edge:
                distances[edge.destination] = distance_via_edge
                heapq.heappush(
                    queue,
                    (
                        distance_via_edge + estimated_distances[edge.destination],
                        route + [edge.destination]
                    )
                )

    return distances



estimated_distances = [
    10, 14, 10, 10, 9, 9, 5, 0, 9, 8, 6, 4, 7, 3
]

nodes = [
    Node([Edge(4, 1),  Edge(5, 1)]),
    Node([Edge(2, 12), Edge(3, 4), Edge(4, 15)]),
    Node([Edge(1, 12), Edge(9, 2), Edge(11, 6)]),
    Node([Edge(1, 4),  Edge(5, 3), Edge(8, 3)]),
    Node([Edge(1, 15), Edge(0, 1), Edge(6, 6)]),
    Node([Edge(0, 1),  Edge(3, 3), Edge(6, 4)]),
    Node([Edge(4, 6),  Edge(5, 4), Edge(10, 1)]),
    Node([Edge(11, 4), Edge(13, 5)]),
    Node([Edge(3, 3),  Edge(9, 1), Edge(10, 5)]),
    Node([Edge(2, 2),  Edge(8, 1), Edge(12, 1)]),
    Node([Edge(6, 1),  Edge(8, 5), Edge(13, 3)]),
    Node([Edge(2, 6),  Edge(7, 4), Edge(12, 5)]),
    Node([Edge(9, 1),  Edge(11, 5), Edge(13, 6)]),
    Node([Edge(7, 5),  Edge(10, 6), Edge(12, 3)]),
]

print(astar(nodes, estimated_distances, 7))
