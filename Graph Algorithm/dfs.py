def dfs_recursive(graph, current_node, visited=None):
    if visited is None:
        visited = set()
        
    # 1. Mark the current node as visited
    visited.add(current_node)
    print(current_node, end=" ")  # Print the node as we visit it
    
    # 2. Recursively visit all unvisited neighbors
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
            
    return visited

# --- Example Usage ---
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("DFS Recursive Traversal:")
dfs_recursive(graph, 'A')
# Output: A B D E C F