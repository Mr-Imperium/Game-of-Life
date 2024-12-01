import streamlit as st
import numpy as np
import time
from game_of_life import GameOfLife

def main():
    st.set_page_config(
        page_title="Colorful Game of Life", 
        page_icon="🌈", 
        layout="wide"
    )
    
    # Custom CSS for better aesthetics
    st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stButton>button {
        color: white;
        background-color: #4A4A4A;
        border: none;
    }
    .stSlider, .stNumberInput {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🌈 Colorful Conway's Game of Life")
    
    # Sidebar for controls
    with st.sidebar:
        st.header("Simulation Controls")
        
        # Advanced grid size with more range
        grid_size = st.slider(
            "Grid Size", 
            min_value=50, 
            max_value=200, 
            value=100, 
            step=10
        )
        
        # Speed and generations controls
        speed = st.slider(
            "Simulation Speed", 
            min_value=0.05, 
            max_value=2.0, 
            value=0.3, 
            step=0.05
        )
        
        max_generations = st.number_input(
            "Max Generations", 
            min_value=10, 
            max_value=1000, 
            value=200
        )
        
        # Color mode selector
        color_mode = st.selectbox(
            "Color Evolution Mode",
            ["Dynamic", "Rainbow", "Monochrome"]
        )
    
    # Initialize game
    game = GameOfLife(size=(grid_size, grid_size))
    
    # Visualization placeholder
    grid_display = st.empty()
    generation_text = st.empty()
    
    # Control buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        start = st.button("▶️ Start")
    with col2:
        pause = st.button("⏸️ Pause")
    with col3:
        reset = st.button("🔄 Reset")
    
    # Simulation state
    if 'running' not in st.session_state:
        st.session_state.running = False
        st.session_state.generation = 0
    
    if reset:
        game.reset((grid_size, grid_size))
        st.session_state.generation = 0
        st.session_state.running = False
    
    if start:
        st.session_state.running = True
    
    if pause:
        st.session_state.running = False
    
    # Main simulation loop
    if st.session_state.running:
        while st.session_state.running and st.session_state.generation < max_generations:
            # Update grid
            grid = game.update()
            
            # Display grid
            grid_display.image(grid, use_column_width=True)
            
            # Update generation text
            generation_text.text(f"Generation: {st.session_state.generation}")
            
            # Increment generation
            st.session_state.generation += 1
            
            # Control speed
            time.sleep(speed)
            
            # Break if max generations reached
            if st.session_state.generation >= max_generations:
                st.session_state.running = False
    
    # Initial display
    grid_display.image(game.color_grid, use_column_width=True)
    generation_text.text(f"Generation: {st.session_state.generation}")

if __name__ == "__main__":
    main()
