
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, node, visited, path, edge_count, paths_with_costs):

    visited.add(node)
    path.append(node)

    if not graph[node]:
        paths_with_costs.append((path[:], edge_count))
    else:
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, path, edge_count + 1, paths_with_costs)

    path.pop()
    visited.remove(node)

def find_all_paths_with_cost(graph, start_node):
    visited = set()  
    paths_with_costs = []  
    dfs(graph, start_node, visited, [], 0, paths_with_costs)
    return paths_with_costs

start_node = 'B'  
paths_with_costs = find_all_paths_with_cost(graph, start_node)

for path, cost in paths_with_costs:
    print(f"Path: {' -> '.join(path)}, Path Cost: {cost}")
