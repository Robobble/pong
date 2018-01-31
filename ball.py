import pygame

white = (255, 255, 255)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()


    def moveHoriz(self, pixels):
        self.rect.x += pixels

    def moveVert(self, pixels):
        self.rect.y += pixels

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)