#reference: https://data-marketing-bk.tistory.com/44
#depth-first search

#1. dfs by python list (stack)

def dfs_list(graph, start_node):
    #visit: will visit, visited: already visit
    visit, visited = list(), list()
    visit.append(start_node)
    print(f"visit: {visit}")

    while visit:
        node = visit.pop()
        if node not in visited:
            visited.append(node)
            print(f"visited: {visited}")
            visit.extend(graph[node])
            print(f"visit: {visit}")

    return visited


#2. dfs by python deque (stack)
from collections import deque
def dfs_deque(graph, start_node):
    visit = deque()
    visited = []
    visit.append(start_node)
    print(f"visit: {visit}")

    while visit:
        node = visit.pop()
        if node not in visited:
            visited.append(node)
            print(f"visited: {visited}")
            visit.extend(graph[node])
            print(f"visit: {visit}")

    return visited


#3. dfs by recursive
def dfs_recursive(graph, start_node, visited=[]):
    visited.append(start_node)
    print(f"visited: {visited}")

    for node in graph[start_node]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

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

    print(f"dfs by list {dfs_list(graph, 'A')}")
    print(f"dfs by deque {dfs_deque(graph, 'A')}")
    print(f"dfs by recursive {dfs_recursive(graph, 'A')}")