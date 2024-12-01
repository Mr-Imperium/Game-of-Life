import streamlit as st
import numpy as np
import time
from game_of_life import GameOfLife

def main():
    st.title("Conway's Game of Life")
    
    # Sidebar configurations
    st.sidebar.header("Simulation Controls")
    
    # Grid size selection
    grid_size = st.sidebar.slider("Grid Size", min_value=10, max_value=100, value=50)
    
    # Speed control
    speed = st.sidebar.slider("Simulation Speed", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
    
    # Initialize game
    game = GameOfLife(size=(grid_size, grid_size))
    
    # Visualization
    grid_display = st.empty()
    
    # Game controls
    start = st.sidebar.button("Start Simulation")
    stop = st.sidebar.button("Stop Simulation")
    reset = st.sidebar.button("Reset Grid")
    
    if reset:
        game = GameOfLife(size=(grid_size, grid_size))
    
    if start:
        while True:
            # Update grid
            grid = game.update()
            
            # Display grid
            grid_display.image(grid * 255, use_column_width=True, clamp=True)
            
            # Delay
            time.sleep(speed)
            
            # Check if stop is pressed
            if stop:
                break
    
    # Initial grid display
    grid_display.image(game.get_grid() * 255, use_column_width=True, clamp=True)

if __name__ == "__main__":
    main()
