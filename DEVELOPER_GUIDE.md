# Snake Game - Developer Guide

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A text editor or IDE (VS Code recommended)
- Git (for version control)

### Quick Setup

```bash
# 1. Clone or navigate to project
cd d:\WorkSpace\GameProject

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the game
python snake_game.py
```

---

## Project Architecture

### File Organization

```
snake_game.py (251 lines)
├── Imports and Initialization
├── Constants (WINDOW_WIDTH, FPS, etc.)
├── Colors Class
├── Direction Enum
├── Snake Class
├── Food Class
├── SnakeGame Class
└── Main Entry Point
```

### Class Hierarchy

```
Colors (Constants)
Direction (Enum)
Snake (Entity)
Food (Entity)
SnakeGame (Engine)
    ├── Contains: Snake instance
    ├── Contains: Food instance
    └── Manages: Game loop, rendering, events
```

---

## Code Structure Breakdown

### 1. Imports (Lines 1-4)
```python
import pygame          # Game engine
import random         # Random food spawning
import sys           # System exit
from enum import Enum # Direction enumeration
```

### 2. Constants (Lines 7-17)
```python
WINDOW_WIDTH = 1000    # Game window width
WINDOW_HEIGHT = 700    # Game window height
GRID_SIZE = 20        # Pixels per cell
GRID_WIDTH = 50       # Calculated grid width
GRID_HEIGHT = 35      # Calculated grid height
FPS = 10              # Game speed (moves/sec)
```

**Customization Tip**: Modify `FPS` to change game difficulty.

### 3. Colors Class (Lines 19-27)
Stores RGB color tuples as class constants.

```python
class Colors:
    BLACK = (10, 10, 10)
    WHITE = (255, 255, 255)
    # ... more colors
```

**Usage**: `Colors.GREEN` returns `(34, 177, 76)`

### 4. Direction Enum (Lines 29-34)
Defines movement vectors for each direction.

```python
class Direction(Enum):
    UP = (0, -1)       # Y decreases
    DOWN = (0, 1)      # Y increases
    LEFT = (-1, 0)     # X decreases
    RIGHT = (1, 0)     # X increases
```

**Usage**: `Direction.UP.value` returns `(0, -1)`

### 5. Snake Class (Lines 36-67)
Manages snake entity and movement logic.

**Key Methods**:
- `__init__()`: Initialize at center with direction RIGHT
- `move()`: Update position based on direction
- `grow()`: Add segment to body
- `check_collision()`: Detect wall/self collision
- `set_direction()`: Change direction safely

**Key Attributes**:
- `body`: List of (x, y) tuples
- `direction`: Current movement direction
- `next_direction`: Buffered next direction

### 6. Food Class (Lines 69-79)
Manages food spawning.

**Key Methods**:
- `__init__()`: Spawn at random location
- `generate()`: Create random (x, y)
- `respawn()`: Move to new location

**Key Attributes**:
- `position`: Current (x, y) coordinate

### 7. SnakeGame Class (Lines 81-251)
Main game engine - most complex class.

**Constructor Phase** (Lines 81-94)
- Initialize Pygame
- Create game window
- Load high score
- Create game objects

**Input Handling** (Lines 104-125)
- Process keyboard events
- Handle window close
- Buffer direction changes
- Handle game over restart

**Game Logic** (Lines 127-145)
- Move snake
- Check food collision
- Update score
- Check collision
- Save high score

**Rendering Methods** (Lines 147-230)
- `draw_gradient_background()`: Animated gradient
- `draw_grid()`: Subtle grid overlay
- `draw_snake()`: Green snake with glow
- `draw_food()`: Red apple with highlight
- `draw_score()`: UI score boxes
- `draw_game_over()`: Game over overlay
- `draw()`: Master render method

**Game Loop** (Lines 232-240)
- Handle input
- Update state
- Render graphics
- Control FPS

---

## Key Algorithms

### Direction-Based Movement
```python
def move(self):
    # Get direction vector
    dx, dy = self.direction.value
    
    # Calculate new head position
    new_head = (head_x + dx, head_y + dy)
    
    # Add to front, remove from back
    self.body.insert(0, new_head)
    self.body.pop()
```

### Collision Detection
```python
def check_collision(self):
    head = self.body[0]
    
    # Wall collision
    if head[0] < 0 or head[0] >= GRID_WIDTH:
        return True
    if head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    
    # Self collision
    if head in self.body[1:]:
        return True
    
    return False
```

### Safe Direction Changing
```python
def set_direction(self, direction):
    # Prevent 180-degree reversal
    if (self.direction.value[0] * -1, 
        self.direction.value[1] * -1) != direction.value:
        self.next_direction = direction
```

### Gradient Background
```python
for y in range(WINDOW_HEIGHT):
    ratio = y / WINDOW_HEIGHT
    
    # Interpolate color
    r = int(Colors.BLACK[0] + 
            (Colors.DARK_BLUE[0] - Colors.BLACK[0]) * ratio)
    
    # Draw horizontal line
    pygame.draw.line(...)
```

---

## Common Modifications

### 1. Change Game Speed
**File**: `snake_game.py` (Line 15)
```python
FPS = 10  # Change to higher number for faster speed
# Examples: 15 (harder), 5 (easier)
```

### 2. Change Window Size
**File**: `snake_game.py` (Lines 10-11)
```python
WINDOW_WIDTH = 1000   # Change width
WINDOW_HEIGHT = 700   # Change height
GRID_SIZE = 20        # Must be divisor of both
```

### 3. Change Color Scheme
**File**: `snake_game.py` (Lines 19-27)
```python
class Colors:
    GREEN = (34, 177, 76)      # Change snake color
    RED = (220, 53, 69)        # Change food color
    # ... modify others
```

### 4. Change Initial Snake Size
**File**: `snake_game.py` (In Snake.__init__)
```python
def __init__(self):
    # Add multiple segments for larger start
    self.body = [
        (GRID_WIDTH // 2, GRID_HEIGHT // 2),
        (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
        (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2),
    ]
```

### 5. Change Score Value
**File**: `snake_game.py` (Line 141)
```python
self.score += 10  # Change to 5, 20, 50, etc.
```

---

## Debugging Tips

### 1. Print Game State
Add this in the `update()` method:
```python
print(f"Snake: {len(self.snake.body)}, Score: {self.score}, Food: {self.food.position}")
```

### 2. Log Collisions
Add in `check_collision()`:
```python
print(f"Collision at {head}")
```

### 3. Check FPS
Add in game loop:
```python
print(f"FPS: {self.clock.get_fps()}")
```

### 4. Verify Input
Add in `handle_input()`:
```python
if event.type == pygame.KEYDOWN:
    print(f"Key pressed: {event.key}")
```

---

## Performance Optimization

### Current Bottlenecks
1. **Gradient drawing**: Redraws every frame
2. **Text rendering**: Could cache surfaces

### Optimization Suggestions

```python
# Cache text surfaces
self.score_surfaces = {}

# In update:
score_str = f"Score: {self.score}"
if score_str not in self.score_surfaces:
    self.score_surfaces[score_str] = \
        self.font_medium.render(score_str, True, Colors.YELLOW)

# In draw:
self.screen.blit(self.score_surfaces[score_str], rect)
```

---

## Testing

### Manual Test Cases

| Test | Steps | Expected Result |
|------|-------|-----------------|
| Move Up | Press ↑ | Snake moves up |
| Move Down | Press ↓ | Snake moves down |
| Move Left | Press ← | Snake moves left |
| Move Right | Press → | Snake moves right |
| Prevent Reverse | Press → then ← | Snake doesn't reverse |
| Eat Food | Move to food | Score +10, snake grows |
| Wall Collision | Move into boundary | Game over |
| Self Collision | Create loop | Game over |
| High Score Save | Beat score, quit, restart | High score persists |
| Restart Game | Press SPACE on game over | Game resets |

### Automated Testing
```python
def test_collision():
    snake = Snake()
    snake.body[0] = (-1, 17)  # Outside boundary
    assert snake.check_collision() == True

def test_grow():
    snake = Snake()
    initial_length = len(snake.body)
    snake.grow()
    assert len(snake.body) == initial_length + 1
```

---

## Deployment

### Creating Executable

Using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed snake_game.py
```

Output in `dist/snake_game.exe`

### Distribution Package
```
SnakeGame_v1.0.zip
├── snake_game.exe
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Troubleshooting

### Issue: Game won't start
**Solution**: Check Pygame installation
```bash
pip install --upgrade pygame
```

### Issue: High score not saving
**Solution**: Check file permissions
```bash
# Ensure highscore.txt is writable
chmod 644 highscore.txt
```

### Issue: Game runs slow
**Solution**: 
- Lower FPS value
- Close other applications
- Check GPU drivers

### Issue: Controls unresponsive
**Solution**:
- Ensure Pygame window is focused
- Check keyboard is working
- Restart the game

---

## Contributing

### Code Style
- Use PEP 8 formatting
- Add docstrings to methods
- Use meaningful variable names
- Comment complex logic

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push to GitHub
git push origin feature/new-feature
```

---

## Resources

### Documentation
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Enum Docs](https://docs.python.org/3/library/enum.html)
- [GitHub Repository](https://github.com/upendrakumar775/SnakeGame)

### Related Tutorials
- Snake Game Implementation
- Pygame Game Loop
- Object-Oriented Game Design

---

## Development Roadmap

### Completed ✅
- Core game mechanics
- Collision detection
- Score system
- High score persistence
- Beautiful graphics

### In Progress 🔄
- Documentation

### Planned 📋
- Sound effects
- Difficulty levels
- Pause functionality
- Leaderboard system

---

## Support & Contact

- **GitHub Issues**: [Report bugs](https://github.com/upendrakumar775/SnakeGame/issues)
- **Documentation**: See API_DOCUMENTATION.md
- **Game Design**: See GAME_DESIGN.md

---

**Guide Version**: 1.0  
**Last Updated**: May 2, 2026  
**Maintainer**: Snake Game Team
