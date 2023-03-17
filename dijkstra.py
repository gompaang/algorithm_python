#dijkstra's algorithm
#pritority queue -> heap
import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    queue = []
    distances[start_node] = 0 #start_node's distance = 0
    heapq.heappush(queue, [start_node, distances[start_node]])
    print(f'queue: {queue}')

    while queue:
        node, distance = heapq.heappop(queue)

        if distance > distances[node]:
            continue

        for new_node, new_distance in graph[node].items():
            d = distance + new_distance
            if d < distances[new_node]:
                distances[new_node] = d
                print(f'distances: {distances}')
                heapq.heappush(queue, [new_node, d])
                print(f'queue: {queue}')

    return distances



if __name__ == '__main__':
    #dijkstra - input: graph, output: shortest length for each node

    # graph = dict()
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }

    print(f"bfs {dijkstra(graph, 'A')}")