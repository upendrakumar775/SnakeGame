import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Colors
class Colors:
    BLACK = (10, 10, 10)
    WHITE = (255, 255, 255)
    GREEN = (34, 177, 76)
    DARK_GREEN = (20, 100, 50)
    RED = (220, 53, 69)
    YELLOW = (255, 193, 7)
    LIGHT_BLUE = (100, 200, 255)
    DARK_BLUE = (30, 100, 180)
    PURPLE = (155, 89, 182)

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
    
    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        self.body.pop()
    
    def grow(self):
        self.body.append(self.body[-1])
    
    def check_collision(self):
        head = self.body[0]
        
        # Check wall collision
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        
        # Check self collision
        if head in self.body[1:]:
            return True
        
        return False
    
    def set_direction(self, direction):
        # Prevent snake from reversing into itself
        if (self.direction.value[0] * -1, self.direction.value[1] * -1) != direction.value:
            self.next_direction = direction

class Food:
    def __init__(self):
        self.position = self.generate()
    
    def generate(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def respawn(self):
        self.position = self.generate()

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("🐍 Snake Game - Beautiful Edition 🐍")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 60)
        self.font_medium = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 30)
        self.font_tiny = pygame.font.Font(None, 24)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.high_score = self.load_high_score()
    
    def load_high_score(self):
        try:
            with open('highscore.txt', 'r') as f:
                return int(f.read())
        except:
            return 0
    
    def save_high_score(self):
        with open('highscore.txt', 'w') as f:
            f.write(str(self.high_score))
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.__init__()
                    elif event.key == pygame.K_q:
                        return False
                else:
                    if event.key == pygame.K_UP:
                        self.snake.set_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(Direction.RIGHT)
                    elif event.key == pygame.K_q:
                        return False
        
        return True
    
    def update(self):
        if not self.game_over:
            self.snake.move()
            
            # Check food collision
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 10
                if self.score > self.high_score:
                    self.high_score = self.score
                self.food.respawn()
            
            # Check game over
            if self.snake.check_collision():
                self.game_over = True
                self.save_high_score()
    
    def draw_gradient_background(self):
        # Create a beautiful gradient background
        for y in range(WINDOW_HEIGHT):
            ratio = y / WINDOW_HEIGHT
            r = int(Colors.BLACK[0] + (Colors.DARK_BLUE[0] - Colors.BLACK[0]) * ratio)
            g = int(Colors.BLACK[1] + (Colors.DARK_BLUE[1] - Colors.BLACK[1]) * ratio)
            b = int(Colors.BLACK[2] + (Colors.DARK_BLUE[2] - Colors.BLACK[2]) * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (WINDOW_WIDTH, y))
    
    def draw_grid(self):
        # Draw subtle grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 60), (x, 0), (x, WINDOW_HEIGHT), 1)
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 60), (0, y), (WINDOW_WIDTH, y), 1)
    
    def draw_snake(self):
        for i, segment in enumerate(self.snake.body):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            
            # Head is brighter
            if i == 0:
                color = Colors.GREEN
                pygame.draw.rect(self.screen, color, (x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4))
                pygame.draw.rect(self.screen, Colors.YELLOW, (x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4), 3)
            else:
                # Body segments get darker
                color_value = max(50, 177 - (i * 5))
                color = (34, color_value, 76)
                pygame.draw.rect(self.screen, color, (x + 3, y + 3, GRID_SIZE - 6, GRID_SIZE - 6))
    
    def draw_food(self):
        x = self.food.position[0] * GRID_SIZE
        y = self.food.position[1] * GRID_SIZE
        
        # Draw apple with glow
        pygame.draw.circle(self.screen, Colors.RED, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
        pygame.draw.circle(self.screen, Colors.YELLOW, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), GRID_SIZE // 2 - 4, 2)
    
    def draw_score(self):
        # Score background
        score_text = f"Score: {self.score}"
        score_surface = self.font_medium.render(score_text, True, Colors.YELLOW)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (20, 20)
        
        # Draw background box
        pygame.draw.rect(self.screen, Colors.PURPLE, (10, 10, score_rect.width + 20, score_rect.height + 10))
        pygame.draw.rect(self.screen, Colors.YELLOW, (10, 10, score_rect.width + 20, score_rect.height + 10), 2)
        self.screen.blit(score_surface, score_rect)
        
        # High score
        high_score_text = f"High Score: {self.high_score}"
        high_score_surface = self.font_small.render(high_score_text, True, Colors.LIGHT_BLUE)
        high_score_rect = high_score_surface.get_rect()
        high_score_rect.topright = (WINDOW_WIDTH - 20, 20)
        
        pygame.draw.rect(self.screen, Colors.DARK_BLUE, (high_score_rect.x - 10, 10, high_score_rect.width + 20, high_score_rect.height + 10))
        pygame.draw.rect(self.screen, Colors.LIGHT_BLUE, (high_score_rect.x - 10, 10, high_score_rect.width + 20, high_score_rect.height + 10), 2)
        self.screen.blit(high_score_surface, high_score_rect)
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(Colors.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, Colors.RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        final_score_text = self.font_medium.render(f"Final Score: {self.score}", True, Colors.YELLOW)
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
        self.screen.blit(final_score_text, final_score_rect)
        
        # Instructions
        restart_text = self.font_small.render("Press SPACE to Restart or Q to Quit", True, Colors.LIGHT_BLUE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        self.screen.blit(restart_text, restart_rect)
    
    def draw(self):
        self.draw_gradient_background()
        self.draw_grid()
        self.draw_food()
        self.draw_snake()
        self.draw_score()
        
        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
