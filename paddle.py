import pygame

BLACK = (0, 0, 0)
SCREEN_LENGTH = 840

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call the parent class (Sprite)
        super().__init__()

        # Sprite's characteristics
        # NOTE: Sprites MUST have "image" attribute
        self.image = pygame.Surface([width, height]) # <= Create box
        self.image.fill(BLACK) # <= Fill box's insides with black
        self.image.set_colorkey(BLACK)
        # self.image.set_colorkey((255, 255, 255))

        # Draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get paddle's dimensions
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):

        # OBJECTIVE: Move paddle upwards

        # Update paddle's Y position
        self.rect.y -= pixels

        # If paddle is going out of bounds, set Y position to 0
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):

        # OBJECTIVE: Move paddle downwards

        # Update paddle's Y position
        self.rect.y += pixels
        # print("Y: {}".format(self.rect.y))

        # If paddle is going out of bounds, set Y position to 620
        if self.rect.y > 620:
            self.rect.y = 620