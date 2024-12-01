import numpy as np
import colorsys

class GameOfLife:
    def __init__(self, size=(100, 100), random_init=True):
        """
        Enhanced Game of Life with more sophisticated grid initialization
        """
        self.size = size
        self.grid = np.zeros(size, dtype=int)
        self.color_grid = np.zeros((*size, 3), dtype=np.uint8)
        
        if random_init:
            # More nuanced random initialization
            self.grid = np.random.choice(
                [0, 1], 
                size=size, 
                p=[0.7, 0.3]  # Increased likelihood of live cells
            )
            self._initialize_color_grid()
    
    def _initialize_color_grid(self):
        """
        Create a color grid based on initial cell states
        Uses HSV color space for more vibrant colors
        """
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.grid[x, y] == 1:
                    # Generate a vibrant, saturated color
                    hue = np.random.random()
                    rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.8)
                    self.color_grid[x, y] = [int(c * 255) for c in rgb]
                else:
                    self.color_grid[x, y] = [20, 20, 20]  # Dark background
    
    def count_neighbors(self, x, y):
        """
        Count live neighbors with wrap-around (toroidal grid)
        """
        neighbors = self.grid[
            (x-1)%self.size[0]:(x+2)%self.size[0], 
            (y-1)%self.size[1]:(y+2)%self.size[1]
        ]
        return np.sum(neighbors) - self.grid[x, y]
    
    def update(self):
        """
        Advanced update method with color evolution
        """
        new_grid = self.grid.copy()
        new_color_grid = self.color_grid.copy()
        
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                neighbors = self.count_neighbors(x, y)
                
                if self.grid[x, y] == 1:
                    # Cell dies
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x, y] = 0
                        new_color_grid[x, y] = [20, 20, 20]  # Fade to black
                    else:
                        # Slightly mutate color of surviving cells
                        hsv = colorsys.rgb_to_hsv(
                            *[c/255 for c in self.color_grid[x, y]]
                        )
                        new_hue = (hsv[0] + 0.05) % 1.0
                        new_rgb = colorsys.hsv_to_rgb(new_hue, 0.8, 0.8)
                        new_color_grid[x, y] = [int(c * 255) for c in new_rgb]
                else:
                    # Cell is born
                    if neighbors == 3:
                        new_grid[x, y] = 1
                        # Inherit color from most common neighbor
                        neighbor_colors = self.get_neighbor_colors(x, y)
                        if len(neighbor_colors):
                            new_color_grid[x, y] = neighbor_colors[0]
                        else:
                            # Random color if no neighbors
                            hue = np.random.random()
                            rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.8)
                            new_color_grid[x, y] = [int(c * 255) for c in rgb]
        
        self.grid = new_grid
        self.color_grid = new_color_grid
        return self.color_grid
    
    def get_neighbor_colors(self, x, y):
        """
        Get colors of live neighbors
        """
        neighbor_colors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = (x + dx) % self.size[0], (y + dy) % self.size[1]
                if self.grid[nx, ny] == 1:
                    neighbor_colors.append(self.color_grid[nx, ny])
        return neighbor_colors
    
    def reset(self, size=None):
        """
        Reset the grid with optional size change
        """
        if size:
            self.size = size
        
        self.grid = np.random.choice(
            [0, 1], 
            size=self.size, 
            p=[0.7, 0.3]
        )
        self._initialize_color_grid()
