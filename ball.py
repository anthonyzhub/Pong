import pygame
from random import randint

BLACK = (0,0,0)

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
        self.velocity = [randint(-5, 8), randint(5, 8)]

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
        self.velocity[0] *= 1.5
        self.velocity[1] *= 1.5
        # print("Velocity now: {}".format(self.velocity))

    def addBoost(self):

        # OBJECTIVE: Temporairly increase ball's velocity when key is pressed

        print("\nBoost enabled")
        print("Velocity before: {}".format(self.velocity))
        self.velocity[0] *= 1.5
        self.velocity[1] *= 1.5
        print("Velocity After: {}".format(self.velocity))

    def removeBoost(self):

        # OBJECTIVE: Reduce speed after passing screen's midpoint

        print("\nBoost disabled")
        print("Velocity before: {}".format(self.velocity))
        self.velocity[0] /= 1.5
        self.velocity[1] /= 1.5
        print("Velocity After: {}".format(self.velocity))