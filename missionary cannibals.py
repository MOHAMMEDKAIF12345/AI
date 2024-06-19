from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, missionaries_right, cannibals_right):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries_right < 0 or self.cannibals_right < 0:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries_right > 0 and self.missionaries_right < self.cannibals_right:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0

    def __eq__(self, other):
        return (self.missionaries == other.missionaries and self.cannibals == other.cannibals and
                self.boat == other.boat and self.missionaries_right == other.missionaries_right and
                self.cannibals_right == other.cannibals_right)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat, self.missionaries_right, self.cannibals_right))

def get_successors(state):
    successors = []
    if state.boat == 'left':
        new_states = [
            State(state.missionaries - 2, state.cannibals, 'right', state.missionaries_right + 2, state.cannibals_right),
            State(state.missionaries - 1, state.cannibals - 1, 'right', state.missionaries_right + 1, state.cannibals_right + 1),
            State(state.missionaries, state.cannibals - 2, 'right', state.missionaries_right, state.cannibals_right + 2),
            State(state.missionaries - 1, state.cannibals, 'right', state.missionaries_right + 1, state.cannibals_right),
            State(state.missionaries, state.cannibals - 1, 'right', state.missionaries_right, state.cannibals_right + 1)
        ]
    else:
        new_states = [
            State(state.missionaries + 2, state.cannibals, 'left', state.missionaries_right - 2, state.cannibals_right),
            State(state.missionaries + 1, state.cannibals + 1, 'left', state.missionaries_right - 1, state.cannibals_right - 1),
            State(state.missionaries, state.cannibals + 2, 'left', state.missionaries_right, state.cannibals_right - 2),
            State(state.missionaries + 1, state.cannibals, 'left', state.missionaries_right - 1, state.cannibals_right),
            State(state.missionaries, state.cannibals + 1, 'left', state.missionaries_right, state.cannibals_right - 1)
        ]
    
    for new_state in new_states:
        if new_state.is_valid():
            new_state.parent = state
            successors.append(new_state)
    return successors

def bfs(initial_state):
    if initial_state.is_goal():
        return initial_state
    
    frontier = deque([initial_state])
    explored = set()
    
    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            return state
        
        explored.add(state)
        
        for child in get_successors(state):
            if child not in explored and child not in frontier:
                frontier.append(child)
    
    return None

def print_solution(solution, max_steps=10):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    
    for i, state in enumerate(path):
        if i >= max_steps:
            break
        print(f"Step {i + 1}: Missionaries: {state.missionaries} Cannibals: {state.cannibals} Boatside: {state.boat}")

if __name__ == "__main__":
    initial_state = State(3, 3, 'left', 0, 0)
    solution = bfs(initial_state)
    
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution exists!")
