import heapq
def prim(graph,start):
    visited =set()
    min_heap=[(0,start)]
    total_cost=0

    while min_heap:
        weight,node=heapq.heappop(min_heap)

        if node in visited:
            continue
        
        visited.add(node)
        total_cost += weight

        print(node ,end=" ")

        for neighbor,edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap,(edge_weight,neighbor))

    print("\nTotal cost: ",total_cost)

graph = {
    'A': [('B', 2), ('C', 6), ('D', 3)],
    'B': [('A', 2), ('D', 8)],
    'C': [('A', 6), ('D', 5)],
    'D': [('A', 3), ('B', 8), ('C', 5)]
}

prim(graph, 'A')