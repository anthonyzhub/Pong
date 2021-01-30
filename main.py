import pygame
from paddle import Paddle

# Constant color declaration
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_WIDTH = 720

def updateScreen(screen, clock, allSpritesList):

    # OBJECTIVE: Update everything displayed on the screen

    # Turn screen black
    screen.fill(BLACK)

    # Draw tennis net dividing the window
    # NOTE: line(surface, color, start pos, end pos, width)
    pygame.draw.line(screen, WHITE, [SCREEN_LENGTH/2, 0], [SCREEN_LENGTH/2, SCREEN_WIDTH], 10)

    # Draw sprites on the window
    allSpritesList.draw(screen)

    # Officially update screen
    pygame.display.flip()

    # Set FPS to 60
    clock.tick(60)

def updatePaddles(keysPressed):

    # UPDATE: Update paddles movements

    if keysPressed[pygame.K_UP]:
        humanPaddle.moveUp(5)

    if keysPressed[pygame.K_DOWN]:
        humanPaddle.moveDown(5)


if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
    pygame.display.set_caption("Anthony's Pong Game")

    # Create paddles
    computerPaddle = Paddle(WHITE, 10, 100)
    computerPaddle.rect.x = 20 # <= Starting X,Y positions
    computerPaddle.rect.y = 300

    humanPaddle = Paddle(WHITE, 10, 100)
    humanPaddle.rect.x = 815
    humanPaddle.rect.y = 300

    # Create a list of all sprites
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(computerPaddle)
    allSpritesList.add(humanPaddle)

    # Boolean variable to play/stop game
    continueGame = True

    # Initialize clock to control screen's FPS
    clock = pygame.time.Clock()

    while continueGame:

        # Look for keyboard inputs
        for event in pygame.event.get():

            if event.type == pygame.QUIT: # NOTE: QUIT refers to "close window" button
                continueGame = False

        # Get input from user
        keysPressed = pygame.key.get_pressed()
        updatePaddles(keysPressed)

        # Update sprites array
        allSpritesList.update()

        # Update screen
        updateScreen(screen, clock, allSpritesList)

    # Quit pygame
    pygame.quit()