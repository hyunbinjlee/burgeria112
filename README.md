# Burgeria 112

Burgeria 112 was my final project for my **15-112 Fundamentals of Programming and Computer Science class** at **Carnegie Mellon University**, named by Bloomberg as one of the **Top Five Best Computer Science Classes in the US** 

I completed this project from November to December 2022. All graphics are also created by me!

This game is inspired by Papa's Burgeria and Overcooked. You are in charge of a fast food drive-thru for seven days. You must be both speedy and careful as this will impact your score! As you progress through the days, you can unlock new toppings like lettuce and tomatoes, but your orders also become more complex. Make it through all seven days and you win!

## How To Play

- **Objective**: Drag and drop items into their proper locations in order to cook them! Create burgers in the sequence given by the order and make sure to place the order in the bag before serving.
- **Tips**:
  - Complete each food item one at a time (e.g., finish a burger before starting fries or drinks).
  - When serving the bag to the window, click on the bag first, then click on the window to move it as desired.
- **Start the Game**:
  - Run `main.py` to start the game.
- **Customization**:
  - Modify the timer in `main.py` (`app.timer`) and `timerFired.py` to change game speed (default: 300000).
  - Adjust `app.levelScores` in `main.py` to set the score required to advance through each level (each value in the list corresponds to a day).

## Features

- Drag-and-drop gameplay mechanics.
- Progression system with increasing difficulty and new toppings as levels advance.
- Win the game by successfully managing the drive-thru for seven days.

## Requirements

- **Python**: The game is built in Python and requires no additional libraries.
- **Files**: Ensure all files and images are downloaded and kept in the same folder for the game to function properly.

## File Overview

- `main.py`: The entry point for the game.
- `foodclasses.py`: Contains classes for different food items.
- `gameMechanics.py`: Manages core game mechanics like order generation and scoring.
- `generateOrder.py`: Handles the generation of customer orders.
- `timerFired.py`: Handles time-related game events.
- `mouseEvents.py`: Handles mouse-based interactions for drag-and-drop functionality.
- `servingfoodclasses.py`: Handles serving functionality for prepared orders.
- `cmu_112_graphics.py`: Custom graphics library used for rendering the game.
- `Design and Documentation/`: Contains design files like the project proposal and storyboard.
- `images/`: Contains all images used in the game.

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/your-username/burgeria112.git
   cd burgeria112
   ```
