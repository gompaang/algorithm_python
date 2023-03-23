# kruskal's algorithm - Minimum Spanning Tree
# Union-Find

def makeset(parent, rank, v):
    parent[v] = v
    rank[v] = 0

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, rank, v1, v2):
    root1 = find(parent, v1)
    root2 = find(parent, v2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    parent = dict()
    rank = dict()
    mst = []

    for v in graph['vertex']:
        makeset(parent, rank, v)

    # sorting edge's weight
    edge = graph['edge']
    edge.sort()

    for e in edge:
        w, v1, v2 = e
        if find(parent, v1) != find(parent, v2):
            union(parent, rank, v1, v2)
            mst.append(e)

    return mst


if __name__ == '__main__':
    graph = {
        'vertex': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'edge': [
            (7, 'A', 'B'),
            (5, 'A', 'D'),
            (7, 'B', 'A'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (7, 'B', 'E'),
            (8, 'C', 'B'),
            (5, 'C', 'E'),
            (5, 'D', 'A'),
            (9, 'D', 'B'),
            (7, 'D', 'E'),
            (6, 'D', 'F'),
            (7, 'E', 'B'),
            (5, 'E', 'C'),
            (7, 'E', 'D'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (6, 'F', 'D'),
            (8, 'F', 'E'),
            (11, 'F', 'G'),
            (9, 'G', 'E'),
            (11, 'G', 'F')
        ]
    }

    print(f'kruskal algorithms: {kruskal(graph)}')