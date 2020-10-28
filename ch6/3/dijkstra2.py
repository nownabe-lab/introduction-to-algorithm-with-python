class Node:
    def __init__(self, distance, edges):
        self.distance = distance
        self.edges = edges


class Edge:
    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost


def heapify(nodes, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min = i

    if left < len(nodes) and nodes[min].distance > nodes[left].distance:
        min = left
    if right < len(nodes) and nodes[min].distance > nodes[right].distance:
        min = right
    if min != i:
        nodes[i], nodes[min] = nodes[min], nodes[i]
        heapify(nodes, min)


def dijkstra(nodes):
    queue = [nodes[0]]

    while len(queue) > 0:
        heapify(queue, 0)
        source = queue.pop(0)

        for edge in source.edges:
            distance_via_edge = source.distance + edge.cost
            if nodes[edge.destination].distance > distance_via_edge:
                nodes[edge.destination].distance = distance_via_edge
                queue.append(nodes[edge.destination])

    return [node.distance for node in nodes]


nodes = [
    Node(0, [Edge(1, 4), Edge(2, 3)]),
    Node(float('inf'), [Edge(2, 1), Edge(3, 1), Edge(4, 5)]),
    Node(float('inf'), [Edge(5, 2)]),
    Node(float('inf'), [Edge(4, 3)]),
    Node(float('inf'), [Edge(6, 2)]),
    Node(float('inf'), [Edge(4, 1), Edge(6, 4)]),
    Node(float('inf'), []),
]

print(dijkstra(nodes))


