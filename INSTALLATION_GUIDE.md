# Snake Game - Installation & Troubleshooting Guide

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Guide](#installation-guide)
3. [Troubleshooting](#troubleshooting)
4. [FAQ](#faq)

---

## System Requirements

### Minimum Requirements
| Component | Requirement |
|-----------|-------------|
| OS | Windows 7+, macOS 10.12+, Linux |
| Python | 3.7 or higher |
| RAM | 512 MB |
| Disk Space | 100 MB |
| Display | 1024×768 or higher |
| GPU | Any with basic 2D support |

### Recommended Specifications
| Component | Recommendation |
|-----------|-----------------|
| OS | Windows 10+, macOS 11+, Ubuntu 18.04+ |
| Python | 3.9 or higher |
| RAM | 2 GB |
| Disk Space | 500 MB |
| Display | 1920×1080 or higher |
| GPU | Dedicated graphics card |

---

## Installation Guide

### Step 1: Install Python

#### Windows
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. **Important**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
```bash
python --version
```

#### macOS
```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip

# Verify
python3 --version
```

### Step 2: Download Project

#### Option A: Clone from GitHub
```bash
git clone https://github.com/upendrakumar775/SnakeGame.git
cd SnakeGame
```

#### Option B: Download ZIP
1. Visit [GitHub Repository](https://github.com/upendrakumar775/SnakeGame)
2. Click "Code" → "Download ZIP"
3. Extract to desired folder
4. Open terminal in extracted folder

### Step 3: Install Dependencies

```bash
# Install Pygame
pip install -r requirements.txt

# Or manually:
pip install pygame==2.5.2
```

**Verify Installation**:
```bash
python -c "import pygame; print(pygame.__version__)"
```
Should output: `2.5.2`

### Step 4: Run the Game

```bash
python snake_game.py
```

**Expected Output**:
- Game window opens (1000×700 pixels)
- Snake visible at center
- Food at random location
- Score displayed at top

---

## Troubleshooting

### Installation Issues

#### Problem: "Python command not found"
```
Error: 'python' is not recognized as an internal or external command
```

**Solution 1: Check Python Installation**
```bash
# Try python3 instead
python3 --version

# If works, create alias
# Windows: Add Python to PATH in Environment Variables
# macOS/Linux: Create alias in ~/.bashrc or ~/.zshrc
```

**Solution 2: Add to PATH (Windows)**
1. Open Environment Variables
2. Click "Edit environment variables for your account"
3. Find "Path" variable
4. Click "Edit"
5. Add: `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python3X`
6. Click OK and restart terminal

**Solution 3: Use full path**
```bash
C:\Python311\python.exe snake_game.py
```

---

#### Problem: "pip command not found"
```
Error: 'pip' is not recognized
```

**Solution 1: Use python -m pip**
```bash
python -m pip install pygame
```

**Solution 2: Upgrade pip**
```bash
python -m pip install --upgrade pip
```

**Solution 3: Check Python installation**
```bash
python -m ensurepip
```

---

#### Problem: "ModuleNotFoundError: No module named 'pygame'"
```
ModuleNotFoundError: No module named 'pygame'
```

**Solution 1: Install Pygame**
```bash
pip install pygame
```

**Solution 2: Check pip location**
```bash
pip show pygame
```

**Solution 3: Use system Python**
```bash
python -m pip install pygame --user
```

**Solution 4: Create virtual environment**
```bash
python -m venv env
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
pip install pygame
```

---

### Runtime Issues

#### Problem: Game window won't open
```
Error: pygame.error: No available video device
```

**Solution 1: Update GPU drivers**
- Windows: NVIDIA/AMD driver update
- macOS: Software Update
- Linux: `sudo apt-get install libsdl2-2.0-0`

**Solution 2: Run in compatibility mode (Windows)**
1. Right-click snake_game.py
2. Select "Properties"
3. "Compatibility" tab
4. Check "Run this program in compatibility mode for"
5. Select Windows 7 Service Pack 1
6. Click Apply

**Solution 3: Install SDL libraries (Linux)**
```bash
sudo apt-get install libsdl2-2.0-0 libsdl2-image-2.0-0
```

---

#### Problem: Game runs very slowly
```
FPS is below 5, game is unplayable
```

**Solution 1: Reduce game speed**
Edit `snake_game.py`, line 15:
```python
FPS = 5  # Instead of 10
```

**Solution 2: Close background applications**
- Task Manager (Windows): Close unnecessary apps
- Activity Monitor (macOS): Quit other apps
- System Monitor (Linux): Kill background processes

**Solution 3: Lower graphics settings**
Edit `snake_game.py`, disable gradient:
```python
def draw_gradient_background(self):
    self.screen.fill(Colors.BLACK)  # Simple fill instead
```

**Solution 4: Update graphics drivers**
- Windows: NVIDIA/AMD/Intel driver
- macOS: Run Software Update
- Linux: `sudo apt-get update && upgrade`

---

#### Problem: Controls are unresponsive
```
Arrow keys don't move snake
```

**Solution 1: Ensure window is focused**
- Click on game window
- Check taskbar shows it's active

**Solution 2: Test keyboard**
```bash
# Create test script:
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key Test")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(f"Key: {event.key}")
```

**Solution 3: Restart the game**
```bash
python snake_game.py
```

**Solution 4: Check keyboard layout**
- Ensure QWERTY layout is active
- Test with NumPad arrows if available

---

#### Problem: High score not saving
```
Highscore.txt not updating
```

**Solution 1: Check file permissions**
```bash
# Windows:
attrib +w highscore.txt

# macOS/Linux:
chmod 644 highscore.txt
```

**Solution 2: Verify file exists**
```bash
# Create if missing
echo "0" > highscore.txt
```

**Solution 3: Check folder permissions**
- Ensure write access to project folder
- Try running as administrator

**Solution 4: Specify full path (Windows)**
Edit snake_game.py:
```python
def load_high_score(self):
    try:
        with open('C:/full/path/to/highscore.txt', 'r') as f:
            return int(f.read())
    except:
        return 0
```

---

#### Problem: Game crashes on startup
```
Traceback (most recent call last):
  File "snake_game.py", line X, in <module>
    ...
AttributeError or ImportError
```

**Solution 1: Check Python version**
```bash
python --version  # Must be 3.7+
```

**Solution 2: Reinstall Pygame**
```bash
pip uninstall pygame
pip install pygame==2.5.2
```

**Solution 3: Check file encoding**
- Save snake_game.py as UTF-8
- Remove any special characters from path

**Solution 4: Full clean install**
```bash
# Remove virtual environment
rm -rf env venv

# Create new one
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install pygame
python snake_game.py
```

---

### Platform-Specific Issues

#### Windows Issues

**Issue: DirectX error**
```
DirectXError: DirectX 9.0 not available
```
**Fix**: Update DirectX
```bash
# Download DirectX End-User Runtime
# https://www.microsoft.com/download/details.aspx?id=8109
```

**Issue: Antivirus blocks game**
**Fix**: Add exception to antivirus
- Windows Defender: Virus & threat protection
- Add folder to exclusions

---

#### macOS Issues

**Issue: "App is damaged"**
**Fix**: Run in terminal instead
```bash
python snake_game.py
```

**Issue: Permission denied**
**Fix**: Grant permissions
```bash
chmod +x snake_game.py
```

---

#### Linux Issues

**Issue: No display found**
**Fix**: Install display server
```bash
sudo apt-get install xvfb
xvfb-run python snake_game.py
```

**Issue: Missing libraries**
**Fix**: Install dependencies
```bash
sudo apt-get install libsdl2-dev libsdl2-image-dev
```

---

## FAQ

### Q: Can I run this on mobile?
**A**: Not directly. The game is built for desktop Python. However, you can:
- Use tools like Kivy to port to mobile
- Use web technologies (Pygame can export to JavaScript)
- Run on Android via Python for Android

### Q: Can I modify the game?
**A**: Yes! The game is open source. See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for modification examples.

### Q: How do I increase difficulty?
**A**: Edit `snake_game.py`, line 15:
```python
FPS = 15  # Higher = faster
```

### Q: Where is my high score saved?
**A**: In `highscore.txt` in the same directory as `snake_game.py`

### Q: Can I play on two computers?
**A**: Current version is single-player only. Multiplayer is planned for future versions.

### Q: The game crashed, how do I recover?
**A**: 
1. Restart the game
2. High score is auto-saved, so it won't be lost
3. If issues persist, see troubleshooting section

### Q: Can I run this headless (no display)?
**A**: Not easily. The game requires a display. For server environments, use:
```bash
xvfb-run python snake_game.py
```

### Q: How do I contribute to development?
**A**: Fork the GitHub repository and submit a pull request. See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)

### Q: Is this game free?
**A**: Yes! Open source under MIT License (or your chosen license)

### Q: What's the highest possible score?
**A**: Theoretically unlimited, but practically:
- Grid size: 1750 cells
- Score per food: 10 points
- Maximum: ~17,500 points (entire grid filled)

### Q: Can I add sound?
**A**: Yes! See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for audio implementation suggestions.

### Q: How do I create an executable?
**A**: 
```bash
pip install pyinstaller
pyinstaller --onefile snake_game.py
# Output in dist/snake_game.exe
```

### Q: Is there a Linux version?
**A**: Yes! It runs on Linux natively. Just follow the installation steps.

---

## Getting Help

### Resources
- **Documentation**: See other .md files
- **GitHub Issues**: [Report bugs](https://github.com/upendrakumar775/SnakeGame/issues)
- **Pygame Docs**: [pygame.org](https://www.pygame.org/docs/)

### Support
1. Check this guide first
2. Read [GAME_DESIGN.md](GAME_DESIGN.md) for game mechanics
3. Read [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for code help
4. Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API reference

---

## Quick Reference

### Common Commands

```bash
# Install
pip install -r requirements.txt

# Run
python snake_game.py

# Test
python -c "import pygame; print(pygame.__version__)"

# Create exe
pyinstaller --onefile snake_game.py

# Clean
rm -rf __pycache__ dist build *.spec
```

### File Locations
- **Game**: `snake_game.py`
- **High Score**: `highscore.txt`
- **Dependencies**: `requirements.txt`
- **Documentation**: `*.md` files

---

**Guide Version**: 1.0  
**Last Updated**: May 2, 2026  
**Status**: Complete

Happy Gaming! 🐍🎮
