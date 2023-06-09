import sys
input = sys.stdin.readline
INF = int(1e9)


def get_smallest_node(graph):
    s = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < s and not visited[i]:
            s = distance[i]
            index = i
    return index


def dijkstra(start, graph):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for j in range(n-1):
        x = get_smallest_node(graph)
        visited[x] = True
        for k in graph[x]:
            cost = distance[x] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost


if __name__ == '__main__':
    n, m = map(int, input().split())  # n:노드 개수, m: 간선 개수
    start = int(input())  # 시작 노드

    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(start, graph)

    for i in range(1, n+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])
