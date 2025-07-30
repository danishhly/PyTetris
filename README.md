# PyTetris - A Classic Retro Tetris Game in Python


## Overview

PyTetris is a classic Tetris game built in Python using the Pygame library. This project demonstrates the use of Object-Oriented Programming (OOP) concepts to create a modular, maintainable, and extensible game. It includes core Tetris mechanics such as block rotation, line clearing, scoring, and next piece preview.

## Features

- Classic Tetris gameplay with smooth controls  
- Object-Oriented design for blocks, grid, and game logic  
- Score tracking and line-clearing mechanics  
- Next piece preview display  
- Game Over screen with restart functionality  
- Background music and sound effects  
- Modern and clean UI with customizable color themes  

## Tech Stack

- Python 3.x  
- Pygame for graphics and input handling  
- Modular OOP design for clear separation of concerns  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/danishhly/PyTetris.git
   cd PyTetris
   ```

2. Install dependencies:

     ```bash
     pip install pygame
     ```

3. Run the game:

    ```bash
    python main.py
    ```

## Usage

Use arrow keys to move and rotate blocks:
  Left/Right: Move piece left/right

  Down: Move piece down faster

  Up: Rotate piece

Press R to restart after game over.

## Code Structure

game.py: Core game logic managing grid, blocks, score, and gameplay flow.

blocks.py: Block shapes and rotation logic.

grid.py: Grid representation and collision detection.

main.py: Game loop and rendering logic.

colors.py: Color palette for UI and blocks.

## Future Improvements

Add levels and increasing difficulty

Implement pause/resume functionality

Add a leaderboard and save high scores

Add animations and particle effects

Mobile-friendly controls and UI


