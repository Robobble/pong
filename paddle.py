import pygame

white = (255, 255, 255)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveup(self, pixels):
        self.rect.y -= pixels

    def movedown(self, pixels):
        self.rect.y += pixels
