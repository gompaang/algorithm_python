import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, x = heapq.heappop(q)
        if distance[x] < dist:
            continue
        for i in graph[x]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


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

    for i in range(1, n + 1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])
