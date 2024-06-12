from collections import deque

def is_valid_state(state, capacity1, capacity2):
    return 0 <= state[0] <= capacity1 and 0 <= state[1] <= capacity2

def bfs(capacity1, capacity2, target):
    # Initialize the queue with the starting state (0, 0) and the set of visited states
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parent = {}

    while queue:
        jug1, jug2 = queue.popleft()
        
        # If we reach the target amount of water in either jug, we return the path
        if jug1 == target or jug2 == target:
            path = []
            while (jug1, jug2) in parent:
                path.append((jug1, jug2))
                jug1, jug2 = parent[(jug1, jug2)]
            path.append((jug1, jug2))
            path.reverse()
            return path
        
        # Generate all possible states from the current state
        possible_states = [
            (capacity1, jug2),  # Fill Jug1
            (jug1, capacity2),  # Fill Jug2
            (0, jug2),          # Empty Jug1
            (jug1, 0),          # Empty Jug2
            (max(0, jug1 - (capacity2 - jug2)), min(jug1 + jug2, capacity2)),  # Pour Jug1 into Jug2
            (min(jug1 + jug2, capacity1), max(0, jug2 - (capacity1 - jug1)))   # Pour Jug2 into Jug1
        ]
        
        for state in possible_states:
            if state not in visited and is_valid_state(state, capacity1, capacity2):
                queue.append(state)
                visited.add(state)
                parent[state] = (jug1, jug2)
    
    return None  # If no solution found

# Example usage
capacity1 = 4
capacity2 = 3
target = 2

path = bfs(capacity1, capacity2, target)
if path:
    for step in path:
        print(step)
else:
    print("No solution found.")
