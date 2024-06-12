# Step 1: Initialize the unweighted graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Step 2: Define the DFS function
def dfs(graph, node, visited, path, edge_count, paths_with_costs):
    # Step 3: Mark the current node as visited
    visited.add(node)
    path.append(node)

    # If it's a leaf node, store the path and the edge count
    if not graph[node]:
        paths_with_costs.append((path[:], edge_count))
    else:
        # Step 5: Recursively visit all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, path, edge_count + 1, paths_with_costs)

    # Step 6: Backtrack
    path.pop()
    visited.remove(node)

# Step 7: Start the DFS traversal
def find_all_paths_with_cost(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    paths_with_costs = []  # List to store paths and their costs
    dfs(graph, start_node, visited, [], 0, paths_with_costs)
    return paths_with_costs

# Example usage
start_node = 'B'  # Starting node for the DFS traversal
paths_with_costs = find_all_paths_with_cost(graph, start_node)

# Print the paths and their costs
for path, cost in paths_with_costs:
    print(f"Path: {' -> '.join(path)}, Path Cost: {cost}")
