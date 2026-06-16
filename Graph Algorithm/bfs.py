from collections import deque

def bfs(graph, start_node):
    # Keep track of visited nodes to avoid infinite loops
    visited = set()
    # Initialize the queue with the starting node
    queue = deque([start_node])
    
    # Mark the starting node as visited
    visited.add(start_node)
    
    # List to store the order of traversal
    traversal_order = []

    while queue:
        # Remove and return the item from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)
        
        # Look at all neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# --- Example Usage ---

# Representing the graph from our walkthrough using an adjacency list
graph = {
    'A': ['C', 'D'],
    'C': ['A', 'B', 'E'],  # Undirected graph example
    'B': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("BFS Traversal starting from node 'A':")
result = bfs(graph, 'A')
print(result)
# Output: ['A', 'B', 'C', 'D', 'E', 'F']