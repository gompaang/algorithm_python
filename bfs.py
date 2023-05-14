# BFS : queue
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited.append(start)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    return visited



if __name__ == '__main__':

    visited = []
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    print(bfs(graph, 1, visited))
