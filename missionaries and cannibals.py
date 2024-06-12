from collections import deque

# Function to check if a state is valid
def is_valid_state(m_left, c_left, m_right, c_right):
    # There should be no more cannibals than missionaries on either side
    if m_left >= 0 and m_right >= 0 and c_left >= 0 and c_right >= 0 and (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):
        return True
    return False

# Function to generate all possible next states
def get_next_states(state):
    m_left, c_left, boat, m_right, c_right = state
    next_states = []
    if boat == 'left':
        # Try all possible moves from left to right
        if is_valid_state(m_left - 2, c_left, m_right + 2, c_right):
            next_states.append((m_left - 2, c_left, 'right', m_right + 2, c_right))
        if is_valid_state(m_left, c_left - 2, m_right, c_right + 2):
            next_states.append((m_left, c_left - 2, 'right', m_right, c_right + 2))
        if is_valid_state(m_left - 1, c_left - 1, m_right + 1, c_right + 1):
            next_states.append((m_left - 1, c_left - 1, 'right', m_right + 1, c_right + 1))
        if is_valid_state(m_left - 1, c_left, m_right + 1, c_right):
            next_states.append((m_left - 1, c_left, 'right', m_right + 1, c_right))
        if is_valid_state(m_left, c_left - 1, m_right, c_right + 1):
            next_states.append((m_left, c_left - 1, 'right', m_right, c_right + 1))
    else:
        # Try all possible moves from right to left
        if is_valid_state(m_left + 2, c_left, m_right - 2, c_right):
            next_states.append((m_left + 2, c_left, 'left', m_right - 2, c_right))
        if is_valid_state(m_left, c_left + 2, m_right, c_right - 2):
            next_states.append((m_left, c_left + 2, 'left', m_right, c_right - 2))
        if is_valid_state(m_left + 1, c_left + 1, m_right - 1, c_right - 1):
            next_states.append((m_left + 1, c_left + 1, 'left', m_right - 1, c_right - 1))
        if is_valid_state(m_left + 1, c_left, m_right - 1, c_right):
            next_states.append((m_left + 1, c_left, 'left', m_right - 1, c_right))
        if is_valid_state(m_left, c_left + 1, m_right, c_right - 1):
            next_states.append((m_left, c_left + 1, 'left', m_right, c_right - 1))
    return next_states

# Function to solve the problem using BFS
def missionaries_and_cannibals():
    # Initial state: 3 missionaries, 3 cannibals on the left side, boat on the left side, 0 missionaries, 0 cannibals on the right side
    initial_state = (3, 3, 'left', 0, 0)
    # Goal state: 0 missionaries, 0 cannibals on the left side, boat on the right side, 3 missionaries, 3 cannibals on the right side
    goal_state = (0, 0, 'right', 3, 3)
    
    # Queue for BFS
    queue = deque([initial_state])
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    # Dictionary to store the path
    parent = {}
    
    while queue:
        state = queue.popleft()
        if state == goal_state:
            # Reconstruct the path from the initial state to the goal state
            path = []
            while state:
                path.append(state)
                state = parent.get(state)
            path.reverse()
            return path
        
        next_states = get_next_states(state)
        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
                parent[next_state] = state

    return None  # If no solution found

# Function to print the solution path
def print_solution(path):
    if path:
        for state in path:
            m_left, c_left, boat, m_right, c_right = state
            print(f"Left: {m_left}M, {c_left}C | Boat: {boat} | Right: {m_right}M, {c_right}C")
    else:
        print("No solution found.")

# Solve the problem and print the solution
solution = missionaries_and_cannibals()
print_solution(solution)
