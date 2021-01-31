import pygame
from random import randint

BLACK = (0,0,0)
X_VELOCITY = 7
Y_VELOCITY = 7

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Initialize parent (Sprite) class
        super().__init__()

        # Define ball's characteristics
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball on the screen
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Set velocity
        # self.velocity = [randint(4, 8), randint(-8, 8)]
        self.velocity = [X_VELOCITY, Y_VELOCITY]

        # Get ball's dimensions
        self.rect = self.image.get_rect()

    def update(self):

        # OBJECTIVE: Update ball's X & Y position

        # Update ball's positioning based on velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):

        # OBJECTIVE: Update ball's velocity when it gets hit

        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def increaseVelocity(self):

        # OBJECTIVE: Increase ball's velocity for difficulty

        # print("\nVelocity before: {}".format(self.velocity))
        self.velocity[0] *= 2
        self.velocity[1] *= 2
        # print("Velocity now: {}".format(self.velocity))