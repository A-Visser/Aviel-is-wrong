import pygame
import random

left = int(input("Enter percent of left turns: "))
right = int(input("Enter percent of right turns: "))
if (left + right > 100):
    print("Error")
straight = 100 - (left + right)
# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle with Buttons")



# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Surface setup
trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.fill(WHITE)
trail_surface.set_colorkey(WHITE)

# Circle setup
x, y = 500, 500
radius = 5
speed_x, speed_y = 0, -1

# Game loop
running = True
paused = False
while running:
    screen.fill(WHITE)  # Keep background white
    screen.blit(trail_surface, (0, 0))
    
# Then draw the main circle
    pygame.draw.circle(screen, BLACK, (x, y), radius)

    # Move circle
    if not paused:
        r = random.randint(1, 100)
        if r <= left:
            speed_x, speed_y = speed_y, -speed_x  # Turn left
        elif r <= left + straight:
            speed_x, speed_y = -speed_x, speed_y  # Turn right
        x += speed_x
        y += speed_y
         # Add current position to trail
        pygame.draw.circle(trail_surface, BLACK, (x, y), 1)

    if x - radius <= 0 or x + radius >= WIDTH:
        paused = True
    if y - radius <= 0 or y + radius >= HEIGHT:
        paused = True

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(100)  # 60 FPS

pygame.quit()
