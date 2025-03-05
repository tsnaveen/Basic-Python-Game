import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLOCK_SIZE = 50  # Size of the blocks, Minecraft-style

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  # Block color (for example, wooden block)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minecraft-Themed FPS')

# Clock for FPS
clock = pygame.time.Clock()

# Player variables
player_pos = [400, 300]
player_angle = 0
player_speed = 5

# Block positions (simple blocks in the world)
blocks = [(300, 200), (500, 400), (100, 100), (700, 500)]

# Functions
def draw_player():
    pygame.draw.circle(screen, WHITE, (int(player_pos[0]), int(player_pos[1])), 20)

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, BROWN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def handle_movement(keys):
    global player_pos, player_angle
    if keys[pygame.K_w]:
        player_pos[0] += player_speed * math.cos(player_angle)
        player_pos[1] += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_pos[0] -= player_speed * math.cos(player_angle)
        player_pos[1] -= player_speed * math.sin(player_angle)
    if keys[pygame.K_a]:
        player_angle -= 0.05
    if keys[pygame.K_d]:
        player_angle += 0.05

def main():
    global player_pos, player_angle
    
    running = True
    while running:
        screen.fill(BLACK)  # Fill the screen with black

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player movement
        keys = pygame.key.get_pressed()
        handle_movement(keys)
        
        # Draw the world (blocks and player)
        draw_blocks()
        draw_player()

        # Update display
        pygame.display.flip()

        # Tick
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
