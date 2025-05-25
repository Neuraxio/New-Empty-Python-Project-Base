import pygame

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Bouncing Ball")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)  # A darker green for trees
RED = (255, 0, 0)  # For the ball

# Ball class
class Ball:
    """
    Represents a bouncing ball in the game.

    Attributes:
        x (float): The x-coordinate of the ball's center.
        y (float): The y-coordinate of the ball's center.
        radius (int): The radius of the ball.
        color (tuple): The color of the ball in RGB format.
        dx (float): The horizontal velocity of the ball.
        dy (float): The vertical velocity of the ball.

    Methods:
        draw(screen): Draws the ball on the given Pygame screen.
        update(): Updates the ball's position based on its velocity.
    """
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt

# Function to draw a tree
def draw_tree(screen, x, y):
        self.x += self.dx
        self.y += self.dy

# Function to draw a tree
def draw_tree(screen, x, y):
    """Draws a simple pine tree shape.
    
    Args:
        screen: The Pygame screen object.
        x: The x-coordinate of the top point of the tree.
        y: The y-coordinate of the top point of the tree.
    """
    point1 = (x, y)
    point2 = (x - 40, y + 100)  # Bottom-left
    point3 = (x + 40, y + 100)  # Bottom-right
    pygame.draw.polygon(screen, GREEN, [point1, point2, point3])

# Create a ball instance
ball = Ball(x=100, y=SCREEN_HEIGHT // 2, radius=15, color=RED, dx=5, dy=3) # Added dy for Y bounce demo

clock = pygame.time.Clock() # New
# Game loop
clock = pygame.time.Clock() # New
# Game loop
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.update() # Update ball's position

        # Bouncing logic
        if ball.x + ball.radius > SCREEN_WIDTH or ball.x - ball.radius < 0:
            ball.dx *= -1
        if ball.y + ball.radius > SCREEN_HEIGHT or ball.y - ball.radius < 0:
            ball.dy *= -1

        screen.fill(WHITE) # Clear screen

        # Draw trees
        draw_tree(screen, x=60, y=SCREEN_HEIGHT - 150)
        draw_tree(screen, x=SCREEN_WIDTH - 60, y=SCREEN_HEIGHT - 150)

        ball.draw(screen) # Draw the ball

        pygame.display.flip()  # Update the full display
        clock.tick(60) # New
except pygame.error as e:
    print(f"A Pygame error occurred: {e}")
finally:
    pygame.quit()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update() # Update ball's position

    # Bouncing logic
    if ball.x + ball.radius > SCREEN_WIDTH or ball.x - ball.radius < 0:
        ball.dx *= -1
    if ball.y + ball.radius > SCREEN_HEIGHT or ball.y - ball.radius < 0:
        ball.dy *= -1

    screen.fill(WHITE) # Clear screen

    # Draw trees
    draw_tree(screen, x=60, y=SCREEN_HEIGHT - 150)
    draw_tree(screen, x=SCREEN_WIDTH - 60, y=SCREEN_HEIGHT - 150)

    ball.draw(screen) # Draw the ball

    pygame.display.flip()  # Update the full display
    clock.tick(60) # New

pygame.quit()
