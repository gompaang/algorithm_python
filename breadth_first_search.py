#breadth_first_search

def bfs(graph, start_node):
    queue, visited = list(), list()
    queue.append(start_node)
    print(f"queue: {queue}")

    while queue:
        node = queue.pop(0)
        visited.append(node)
        print(f"visited {visited}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                print(f"queue: {queue}")

    return visited



if __name__ == '__main__':
    #bfs- input: graph, output: order search node

    # graph = dict()
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'G', 'H', 'I'],
        'D': ['B', 'E', 'F'],
        'E': ['D'],
        'F': ['D'],
        'G': ['C'],
        'H': ['C'],
        'I': ['C', 'J'],
        'J': ['I'],
    }

    print(f"bfs {bfs(graph, 'A')}")