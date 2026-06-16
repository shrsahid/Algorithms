import heapq

def dijkstra(graph, start):
    # graph format: {'A': [('B', 4), ('C', 1)], ...}
    
    # Initialize distances to infinity, and start node to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority Queue stores tuples: (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we found a longer path to this node already processed, skip it
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Relaxation step: If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Example Graph Representation
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 3)],
    'C': [('B', 2), ('D', 6)],
    'D': []
}

shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from node A:")
for node, distance in shortest_paths.items():
    print(f"To {node} : {distance}")