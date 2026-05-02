# 🐍 Beautiful Snake Game

A stunning Snake game built with Python and Pygame featuring beautiful graphics, smooth gameplay, and score tracking.

## Features

✨ **Beautiful Graphics**
- Gradient background with subtle grid
- Colorful snake with glowing head
- Shiny red apple food
- Smooth animations

📊 **Score System**
- Real-time score display
- High score tracking (saved to disk)
- Score increases by 10 points per food eaten

🎮 **Smooth Gameplay**
- Responsive controls
- Smooth snake movement
- Collision detection
- Game over screen with restart option

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

## How to Play

Run the game:
```bash
python snake_game.py
```

### Controls
- **Arrow Keys** - Move the snake (↑ ↓ ← →)
- **Q** - Quit the game
- **SPACE** - Restart after game over

### Gameplay
1. Use arrow keys to control the snake
2. Eat the red apples to grow and increase your score
3. Avoid hitting walls and yourself
4. Try to beat your high score!

## Game Features

### Score Display
- Current score shown in top-left corner (purple box)
- High score displayed in top-right corner (blue box)
- High score is automatically saved when you beat it

### Beautiful UI Elements
- **Gradient background**: Dark gradient from black to dark blue
- **Grid pattern**: Subtle grid for better visibility
- **Snake**: Green body with yellow glowing border on head
- **Food**: Red circles with yellow highlights (looks like apples)
- **Game Over Screen**: Semi-transparent overlay with final score

## Technical Details

- **Grid Size**: 20x20 pixels
- **Game Speed**: 10 FPS (adjustable by changing FPS constant)
- **Window Size**: 1000x700 pixels
- **Built with**: Python 3 + Pygame 2

## Tips for High Score

- Plan your movements ahead
- Try to create patterns or spirals
- Avoid corners when possible
- Stay calm and focused!

## Customization

You can customize the game by editing constants in `snake_game.py`:
- `FPS` - Adjust game speed
- `WINDOW_WIDTH` and `WINDOW_HEIGHT` - Change window size
- `Colors` class - Modify color scheme
- `GRID_SIZE` - Adjust grid square size

## Troubleshooting

### Pygame not found
```bash
pip install --upgrade pygame
```

### Game runs slowly
- Lower the FPS value in the code
- Close other applications

### High score not saving
- Ensure you have write permissions in the game directory
- Check that `highscore.txt` file exists

## Enjoy! 🎮🐍

Have fun playing the Snake game! Challenge yourself to beat your high score!
