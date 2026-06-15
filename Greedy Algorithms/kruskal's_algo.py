def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v

        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u

        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(vertices, edges):

    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_cost = 0

    for u, v, weight in edges:

        if find(parent, u) != find(parent, v):

            union(parent, rank, u, v)

            mst.append((u, v, weight))
            total_cost += weight

    print("MST Edges:")
    for edge in mst:
        print(edge)

    print("Total Cost =", total_cost)


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 2),
    ('A', 'D', 3),
    ('C', 'D', 5),
    ('A', 'C', 6),
    ('B', 'D', 8)
]

kruskal(vertices, edges)