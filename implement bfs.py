from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, 0, [start])])
    visited = set()

    while queue:
        current_node, current_cost, path = queue.popleft()
        if current_node == goal:
            return current_cost, path
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, current_cost + cost, path + [neighbor]))
    
    return None  

graph = {
    'a': [('b', 1), ('c', 4)],
    'b': [('a', 1), ('d', 2), ('e', 5)],
    'c': [('a', 4), ('f', 3)],
    'd': [('b', 2)],
    'e': [('b', 5), ('f', 1)],
    'f': [('c', 3), ('e', 1)]
}

start_node = 'a'
goal_node = 'f'
result = bfs(graph, start_node, goal_node)

if result:
    path_cost, path = result
    print(f"The path cost from {start_node} to {goal_node} is: {path_cost}")
    print(f"The path from {start_node} to {goal_node} is: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
