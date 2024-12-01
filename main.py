import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Set page config for dark theme
st.set_page_config(page_title="Neon Conway's Game of Life", page_icon="🧬", layout="wide")

# Custom CSS for neon effect and dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    .stButton>button {
        color: #00ff00;
        background-color: #1a1a1a;
        border: 2px solid #00ff00;
        border-radius: 5px;
    }
    .stButton>button:hover {
        color: #000000;
        background-color: #00ff00;
    }
    .stSlider>div>div>div>div {
        background-color: #00ff00;
    }
    .stSlider>div>div>div>div>div {
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Initialize game state
@st.cache_data
def initialize_game(width, height):
    return np.random.choice([0, 1, 2], size=(height, width), p=[0.8, 0.1, 0.1])

# Update game state
def update_game(frame):
    new_frame = frame.copy()
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            total = int((frame[i, (j-1)%frame.shape[1]] > 0) + (frame[i, (j+1)%frame.shape[1]] > 0) + 
                        (frame[(i-1)%frame.shape[0], j] > 0) + (frame[(i+1)%frame.shape[0], j] > 0) + 
                        (frame[(i-1)%frame.shape[0], (j-1)%frame.shape[1]] > 0) + (frame[(i-1)%frame.shape[0], (j+1)%frame.shape[1]] > 0) + 
                        (frame[(i+1)%frame.shape[0], (j-1)%frame.shape[1]] > 0) + (frame[(i+1)%frame.shape[0], (j+1)%frame.shape[1]] > 0))
            if frame[i, j] > 0:
                if (total < 2) or (total > 3):
                    new_frame[i, j] = 0
                else:
                    new_frame[i, j] = frame[i, j]  # Keep the same color
            else:
                if total == 3:
                    # New cell born, randomly choose between red and green
                    new_frame[i, j] = np.random.choice([1, 2])
    return new_frame

# Streamlit app
st.title("🧬 Neon Conway's Game of Life")

# Sidebar controls
st.sidebar.title("🎛️ Controls")
width = st.sidebar.slider("Width", 10, 100, 50)
height = st.sidebar.slider("Height", 10, 100, 50)
frame_rate = st.sidebar.slider("Frame Rate", 1, 30, 10)

# Initialize game state
if 'game_state' not in st.session_state:
    st.session_state.game_state = initialize_game(width, height)
    st.session_state.game_running = False

# Buttons
col1, col2, col3 = st.columns(3)
start_stop = col1.button("▶️ Start/Stop")
step = col2.button("⏭️ Step")
reset = col3.button("🔄 Reset")

if start_stop:
    st.session_state.game_running = not st.session_state.game_running

if step:
    st.session_state.game_state = update_game(st.session_state.game_state)

if reset:
    st.session_state.game_state = initialize_game(width, height)
    st.session_state.game_running = False

# Game visualization
fig, ax = plt.subplots(figsize=(10, 10))
cmap = ListedColormap(['black', '#ff0000', '#00ff00'])  # Black background, neon red, neon green
img = ax.imshow(st.session_state.game_state, cmap=cmap, interpolation='nearest')
ax.axis('off')
plt.tight_layout()
game_plot = st.pyplot(fig)

# Main game loop
if st.session_state.game_running:
    st.session_state.game_state = update_game(st.session_state.game_state)
    img.set_data(st.session_state.game_state)
    game_plot.pyplot(fig)
    plt.close(fig)
    st.rerun()

