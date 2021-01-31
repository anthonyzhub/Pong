import pygame
from paddle import Paddle
from ball import Ball

# Constant color declaration
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_WIDTH = 720
SCREEN_MID = SCREEN_LENGTH/2

def updateScreen(screen, clock, allSpritesList):

    # OBJECTIVE: Update everything displayed on the screen

    # Turn screen black
    screen.fill(BLACK)

    # Draw tennis net dividing the window
    # NOTE: line(surface, color, start pos, end pos, width)
    pygame.draw.line(screen, WHITE, [SCREEN_LENGTH//2, 0], [SCREEN_LENGTH//2, SCREEN_WIDTH], 10)

    # Update scoreboard
    font = pygame.font.Font(None, 74)
    text = font.render(str(computerScore), 1, WHITE)
    screen.blit(text, (SCREEN_MID//2, 10))

    text = font.render(str(humanScore), 1, WHITE)
    screen.blit(text, (SCREEN_MID + (SCREEN_MID//2), 10))

    # Draw sprites on the window
    allSpritesList.draw(screen)

    # Officially update screen
    pygame.display.flip()

    # Set FPS to 60
    clock.tick(60)

def updatePaddles(keysPressed):

    # OBJECTIVE: Update paddles' movements

    if keysPressed[pygame.K_UP]:
        humanPaddle.moveUp(5)

    if keysPressed[pygame.K_DOWN]:
        humanPaddle.moveDown(5)

def updateBall(ball, computerScore, humanScore):

    # OBJECTIVE: Update ball's movement

    if ball.rect.x >= SCREEN_LENGTH - 10:
        ball.velocity[0] = -ball.velocity[0]
        computerScore += 1
        # print("Decreasing X velocity")

    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        humanScore += 1
        # print("Increasing X velocity")

    if ball.rect.y > SCREEN_WIDTH - 10:
        ball.velocity[1] = -ball.velocity[1]
        # print("Decreasing Y velocity")

    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
        # print("Increasing Y velocity")

    return computerScore, humanScore

if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
    pygame.display.set_caption("Anthony's Pong Game")

    # Initialize scores
    computerScore = 0
    humanScore = 0

    # Create paddles
    computerPaddle = Paddle(WHITE, 10, 100)
    computerPaddle.rect.x = 20 # <= Starting X,Y positions
    computerPaddle.rect.y = 300

    humanPaddle = Paddle(WHITE, 10, 100)
    humanPaddle.rect.x = 815
    humanPaddle.rect.y = 300

    # Create the ball
    ball = Ball(WHITE, 10, 10)
    ball.rect.x = (computerPaddle.rect.x + humanPaddle.rect.x) // 2
    ball.rect.y = 300

    # Create a list of all sprites
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(computerPaddle)
    allSpritesList.add(humanPaddle)
    allSpritesList.add(ball)

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

        # Call update() from all sprites
        allSpritesList.update()

        # Update ball's movement
        computerScore, humanScore = updateBall(ball, computerScore, humanScore)

        # Detect collisions between paddles and ball
        if pygame.sprite.collide_mask(ball, computerPaddle) or pygame.sprite.collide_mask(ball, humanPaddle):
            ball.bounce()

        # Update screen
        updateScreen(screen, clock, allSpritesList)

    # Quit pygame
    pygame.quit()