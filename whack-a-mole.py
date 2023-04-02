import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Set the dimensions of the mole and the hammer
MOLE_WIDTH = 50
MOLE_HEIGHT = 50
HAMMER_WIDTH = 50
HAMMER_HEIGHT = 50

# Set the speed of the mole
MOLE_SPEED = 5

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Set up the clock
clock = pygame.time.Clock()

# Load the images
mole_image = pygame.image.load("mole.png").convert_alpha()
hammer_image = pygame.image.load("hammer.png").convert_alpha()


# Scale the images to the desired size
mole_image = pygame.transform.scale(mole_image, (MOLE_WIDTH, MOLE_HEIGHT))
hammer_image = pygame.transform.scale(
    hammer_image, (HAMMER_WIDTH, HAMMER_HEIGHT))

# Set the color key for the images
mole_image.set_colorkey((0, 255, 0))
hammer_image.set_colorkey((0, 255, 0))

# Set up the font
font = pygame.font.SysFont(None, 36)

# Define the function to create a new mole


def create_mole():
    x = random.randint(0, SCREEN_WIDTH - MOLE_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT - MOLE_HEIGHT)
    return pygame.Rect(x, y, MOLE_WIDTH, MOLE_HEIGHT)


# Initialize the game state
score = 0
time_remaining = 60
mole = create_mole()
hammer = pygame.Rect(0, 0, HAMMER_WIDTH, HAMMER_HEIGHT)

# Run the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammer.center = event.pos

    # Update the hammer position
    hammer.center = pygame.mouse.get_pos()

    # Move the mole
    mole.move_ip(0, MOLE_SPEED)

    # Check if the mole has reached the bottom of the screen
    if mole.top > SCREEN_HEIGHT:
        mole = create_mole()
        time_remaining -= 1

    # Check for collision between the hammer and the mole
    if hammer.colliderect(mole):
        score += 1
        mole = create_mole()

    # Draw the screen
    screen.fill(BLACK)
    screen.blit(mole_image, mole)
    screen.blit(hammer_image, hammer)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    time_text = font.render("Time: " + str(time_remaining), True, WHITE)
    screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

    # Check if the time has run out
    if time_remaining == 0:
        running = False

# Show the final score
final_score_text = font.render("Final Score: " + str(score), True, WHITE)
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() //
            2, SCREEN_HEIGHT // 2 - final_score_text.get_height() // 2))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
