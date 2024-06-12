import heapq

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan_distance(state):
    distance = 0
    for i in range(1, 9):
        ix, iy = divmod(state.index(i), 3)
        gx, gy = divmod(goal_state.index(i), 3)
        distance += abs(ix - gx) + abs(iy - gy)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    blank_row, blank_col = divmod(blank_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move in moves:
        new_row, new_col = blank_row + move[0], blank_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
            neighbors.append(tuple(new_state))
    
    return neighbors

def a_star_search(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0 + manhattan_distance(initial_state), 0, initial_state, []))
    visited = set()
    visited.add(initial_state)

    while priority_queue:
        _, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(priority_queue, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, path + [current_state]))

    return None

def print_path(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)

path = a_star_search(initial_state)

if path:
    print("Solution found!")
    print_path(path)
else:
    print("No solution exists.")
