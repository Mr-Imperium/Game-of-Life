import numpy as np

class GameOfLife:
    def __init__(self, size=(50, 50), random_init=True):
        """
        Initialize the Game of Life grid
        
        Args:
        - size: Tuple of (width, height) for the grid
        - random_init: Whether to randomly initialize the grid
        """
        self.size = size
        self.grid = np.zeros(size, dtype=int)
        
        if random_init:
            self.grid = np.random.choice([0, 1], size=size, p=[0.85, 0.15])
    
    def count_neighbors(self, x, y):
        """
        Count live neighbors for a given cell
        
        Args:
        - x: x-coordinate of the cell
        - y: y-coordinate of the cell
        
        Returns:
        Number of live neighbors
        """
        # Create a slice of 3x3 grid around the cell, handling edge cases
        neighbors = self.grid[max(0, x-1):min(self.size[0], x+2), 
                              max(0, y-1):min(self.size[1], y+2)]
        
        # Subtract the cell itself from the count
        return np.sum(neighbors) - self.grid[x, y]
    
    def update(self):
        """
        Apply Game of Life rules to update the grid
        
        Returns:
        Updated grid
        """
        new_grid = self.grid.copy()
        
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                neighbors = self.count_neighbors(x, y)
                
                # Game of Life rules
                if self.grid[x, y] == 1:
                    # Live cell dies from underpopulation or overpopulation
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x, y] = 0
                else:
                    # Dead cell becomes alive with exactly 3 neighbors
                    if neighbors == 3:
                        new_grid[x, y] = 1
        
        self.grid = new_grid
        return self.grid
    
    def get_grid(self):
        """
        Get current grid state
        
        Returns:
        Current grid
        """
        return self.grid
