# Snake Game - Quick Reference Guide

## 📚 Documentation Files

This project includes comprehensive documentation:

| Document | Purpose | Best For |
|----------|---------|----------|
| **README.md** | Overview & quick start | New players |
| **API_DOCUMENTATION.md** | Complete API reference | Developers |
| **GAME_DESIGN.md** | Game mechanics & design | Designers |
| **DEVELOPER_GUIDE.md** | Code structure & modification | Programmers |
| **INSTALLATION_GUIDE.md** | Setup & troubleshooting | Installation issues |
| **QUICK_REFERENCE.md** | This file | Quick lookup |

---

## 🎮 Game Controls

| Key | Action |
|-----|--------|
| ⬆️ UP | Move snake up |
| ⬇️ DOWN | Move snake down |
| ⬅️ LEFT | Move snake left |
| ➡️ RIGHT | Move snake right |
| Q | Quit game |
| SPACE | Restart (on game over) |

---

## 📊 Game Statistics

| Metric | Value |
|--------|-------|
| **Grid Size** | 50 × 35 cells |
| **Window Size** | 1000 × 700 pixels |
| **Cell Size** | 20 × 20 pixels |
| **Game Speed** | 10 FPS |
| **Points per Food** | 10 |
| **Max Snake Length** | 1750 |

---

## 📁 Project Structure

```
GameProject/
├── snake_game.py                 # Main game (251 lines)
├── requirements.txt              # Dependencies
├── README.md                     # User guide
├── API_DOCUMENTATION.md          # API reference
├── GAME_DESIGN.md               # Game design doc
├── DEVELOPER_GUIDE.md           # Developer guide
├── INSTALLATION_GUIDE.md        # Installation help
├── QUICK_REFERENCE.md           # This file
└── highscore.txt                # High score storage
```

---

## 🚀 Quick Start

### Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the game
python snake_game.py
```

### First Game
1. Game window opens
2. Press arrow keys to control snake
3. Eat red apples to grow
4. Avoid walls and your own body
5. Press Q to quit or SPACE to restart

---

## 🎨 Color Palette

| Element | Color | RGB |
|---------|-------|-----|
| Background | Black → Dark Blue | (10,10,10) → (30,100,180) |
| Snake Head | Bright Green | (34, 177, 76) |
| Snake Body | Dark Green | (20, 100, 50) |
| Food | Red | (220, 53, 69) |
| Score Text | Yellow | (255, 193, 7) |
| Grid | Dark Gray | (40, 40, 60) |

---

## 💻 Code Organization

### Main Classes

```python
class Snake:              # Snake entity
    move()              # Move one step
    grow()              # Add body segment
    check_collision()   # Detect collision
    set_direction()     # Change direction

class Food:              # Food entity
    generate()          # Random position
    respawn()          # New location

class SnakeGame:         # Game engine
    handle_input()      # Process events
    update()           # Game logic
    draw()             # Render graphics
    run()              # Main loop
```

---

## 🔧 Common Modifications

### Change Game Speed
**File**: `snake_game.py` Line 15
```python
FPS = 10  # Change number (higher = faster)
```

### Change Colors
**File**: `snake_game.py` Lines 19-27
```python
class Colors:
    GREEN = (34, 177, 76)  # Modify this
```

### Change Window Size
**File**: `snake_game.py` Lines 10-11
```python
WINDOW_WIDTH = 1000   # New width
WINDOW_HEIGHT = 700   # New height
```

### Change Score Value
**File**: `snake_game.py` Line 141
```python
self.score += 10  # Change to 5, 20, etc.
```

---

## 🐛 Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Pygame not found | `pip install pygame` |
| Game slow | Lower FPS value in code |
| Controls unresponsive | Click game window to focus |
| High score not saving | Check file permissions |
| Game won't start | Update GPU drivers |

---

## 📈 Scoring System

```
Food Eaten → +10 Points
Score = # Foods × 10

Examples:
1 food  → 10 points
10 foods → 100 points
100 foods → 1000 points
```

---

## 🎯 Game Mechanics

### Movement
- Snake moves automatically in current direction
- Player changes direction (queued for next move)
- Cannot reverse 180 degrees

### Collision Types
1. **Wall**: Head touches boundary → Game Over
2. **Self**: Head touches body → Game Over
3. **Food**: Head touches apple → Grow + Score

### Spawning
- Snake starts at center (25, 17)
- Food spawns at random grid location
- Both avoid undefined positions

---

## 📱 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 7+, macOS 10.12+, Linux |
| **Python** | 3.7+ |
| **RAM** | 512 MB |
| **Disk** | 100 MB |
| **Display** | 1024×768+ |

---

## 🔗 Useful Links

| Link | Purpose |
|------|---------|
| [GitHub Repo](https://github.com/upendrakumar775/SnakeGame) | Source code & issues |
| [Pygame Docs](https://www.pygame.org/docs/) | Framework documentation |
| [Python Docs](https://docs.python.org/3/) | Language reference |

---

## 💡 Tips & Tricks

### For Players
1. **Plan ahead** - Think 2-3 moves ahead
2. **Avoid corners** - Easier to escape from center
3. **Create patterns** - Spiral or zig-zag movements
4. **Stay calm** - Slower, deliberate moves work better

### For Developers
1. **Use virtual environment** - `python -m venv env`
2. **Read code comments** - Understand the flow
3. **Start small** - Add one feature at a time
4. **Test often** - Verify changes work

---

## 📝 Performance Notes

| Aspect | Value |
|--------|-------|
| Game Update Rate | 10 Hz (100ms per move) |
| Render Rate | ~60 Hz (Pygame default) |
| Memory Usage | 15-20 MB |
| CPU Usage | <5% idle |
| Startup Time | <1 second |

---

## 🎓 Learning Resources

### For Players
- [Snake Game Rules](https://en.wikipedia.org/wiki/Snake_(video_game))
- [Classic Snake Tips](https://www.youtube.com/results?search_query=snake+game+tips)

### For Programmers
- [Pygame Tutorial](https://www.pygame.org/wiki/tutorials)
- [Object-Oriented Python](https://docs.python.org/3/tutorial/classes.html)
- [Game Loop Architecture](https://en.wikipedia.org/wiki/Game_loop)

---

## 🔐 Data Storage

### High Score
- **File**: `highscore.txt`
- **Format**: Plain text integer
- **Auto-save**: When game over (if beaten)
- **Location**: Project directory

### Example Content
```
1250
```

---

## 🎮 Game States

```
INIT
  ↓
PLAYING ← Player input
  ↓ (Collision)
GAME_OVER
  ↓ (Q pressed)
EXIT
```

---

## 🚨 Error Messages Guide

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: pygame` | Pygame not installed | `pip install pygame` |
| `FileNotFoundError: pygame` | Wrong Python/package manager | Use `python -m pip install` |
| `No available video device` | GPU driver issue | Update video drivers |
| `Permission denied` | File write issue | Check folder permissions |

---

## 🌟 Feature Checklist

### Implemented ✅
- [x] Snake movement (4 directions)
- [x] Food spawning (random)
- [x] Collision detection
- [x] Score system
- [x] High score persistence
- [x] Beautiful graphics
- [x] Game over screen
- [x] Restart functionality

### Planned 📋
- [ ] Sound effects
- [ ] Difficulty levels
- [ ] Pause feature
- [ ] Leaderboard
- [ ] Power-ups
- [ ] Obstacles
- [ ] Multiplayer

---

## 📞 Support

### Need Help?
1. Check **INSTALLATION_GUIDE.md** for setup issues
2. Read **DEVELOPER_GUIDE.md** for code questions
3. Review **GAME_DESIGN.md** for game mechanics
4. Check **API_DOCUMENTATION.md** for function details

### Report Issues
- GitHub: [Submit Issue](https://github.com/upendrakumar775/SnakeGame/issues)
- Include: OS, Python version, error message

---

## 📄 License & Credits

- **Project**: Beautiful Snake Game
- **Version**: 1.0
- **Date**: May 2, 2026
- **Engine**: Python 3.7+ with Pygame 2.5.2
- **Author**: Snake Game Developer

---

## 🎉 Quick Commands

```bash
# Install & run
pip install -r requirements.txt && python snake_game.py

# Create executable
pyinstaller --onefile --windowed snake_game.py

# Run tests
python -m pytest

# Format code
python -m black snake_game.py

# Check syntax
python -m py_compile snake_game.py
```

---

## 📊 File Sizes

| File | Size | Description |
|------|------|-------------|
| snake_game.py | 9.6 KB | Main game |
| README.md | 2.7 KB | User guide |
| Requirements | 15 B | Dependencies |
| **Total** | **~60 KB** | All docs |

---

**Last Updated**: May 2, 2026  
**Status**: Complete  
**Next**: Implement features from Planned list

---

**Happy Gaming! 🐍🎮**
