import random

class VacuumCleaner:
    def _init_(self, grid):
        self.grid = grid
        self.current_pos = (0, 0)
        self.direction = 'right'

    def move(self):
        x, y = self.current_pos
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0  # Clean the current cell
        if self.direction == 'right':
            if y < len(self.grid[0]) - 1:
                y += 1
            else:
                y = len(self.grid[0]) - 1
                self.direction = 'down'
        elif self.direction == 'down':
            if x < len(self.grid) - 1:
                x += 1
            else:
                x = len(self.grid) - 1
                self.direction = 'left'
        elif self.direction == 'left':
            if y > 0:
                y -= 1
            else:
                y = 0
                self.direction = 'up'
        elif self.direction == 'up':
            if x > 0:
                x -= 1
            else:
                x = 0
                self.direction = 'right'
        self.current_pos = (x, y)

    def clean_grid(self):
        while any(1 in row for row in self.grid):
            self.move()
            if all(0 in row for row in self.grid):
                break

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

# Example usage:
ROWS, COLS = 5, 5
grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

vacuum_cleaner = VacuumCleaner(grid)
print("Initial Grid:")
vacuum_cleaner.print_grid()

vacuum_cleaner.clean_grid()
print("Final Grid:")
vacuum_cleaner.print_grid()
