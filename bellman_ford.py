# bellman-ford algorithm

def bellman_ford(graph, start_node):
    dis = {node: float('inf') for node in graph}
    dis[start_node] = 0

    for i in range(len(graph)-1):
        for node in graph:
            # node -> neighbor
            for neighbor in graph[node]:
                if dis[neighbor] > dis[node] + graph[node][neighbor]:
                    dis[neighbor] = dis[node] + graph[node][neighbor]

    # negative cycle check
    for node in graph:
        for neighbor in graph[node]:
            if dis[neighbor] > dis[node] + graph[node][neighbor]:
                return False

    return dis


if __name__ == '__main__':
    # bellman_ford - input: graph, start_node, output: distances of nodes

    # graph = dict()
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }

    print(f"bellman_ford: {bellman_ford(graph,'A')}")