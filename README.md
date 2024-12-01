# 🌈 Colorful Conway's Game of Life

## Overview
This is an interactive, visually stunning implementation of Conway's Game of Life using Python, NumPy, and Streamlit. The project goes beyond the traditional black and white cellular automaton by introducing dynamic, evolving color patterns.

## Features
- 🎨 Vibrant, color-evolving cellular automaton
- 🌐 Toroidal grid with wrap-around edges
- 🎛️ Interactive controls for:
  - Grid size
  - Simulation speed
  - Maximum generations
- 🖥️ Modern, dark-mode UI
- 🔄 Real-time generation tracking
- 🌟 Unique color inheritance and mutation mechanics

## Prerequisites
- Python 3.8+
- pip

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/colorful-game-of-life.git
cd colorful-game-of-life
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
streamlit run app.py
```

## How It Works

### Cellular Automaton Rules
The simulation follows Conway's classic Game of Life rules:
- Live cells with < 2 live neighbors die (underpopulation)
- Live cells with 2-3 live neighbors survive
- Live cells with > 3 live neighbors die (overpopulation)
- Dead cells with exactly 3 live neighbors become alive

### Color Evolution
Unlike traditional implementations, this version introduces:
- Dynamic color mutation
- Color inheritance for new cells
- Vibrant, evolving visual patterns

### Grid Mechanics
- Toroidal grid ensures continuous space
- Wrap-around edges create interesting pattern interactions

## UI Controls
- **Grid Size**: Adjust the simulation area (50-200 cells)
- **Simulation Speed**: Control update frequency
- **Max Generations**: Limit simulation duration
- **Start/Pause/Reset**: Control simulation state

## Technologies
- Python
- NumPy
- Streamlit
- Colorsys (for color transformations)

## Customization
Modify `game_of_life.py` to:
- Change initial population probability
- Adjust color generation logic
- Implement custom cellular automaton rules

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License

## Acknowledgments
Inspired by John Conway's original Game of Life concept.
