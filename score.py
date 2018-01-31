import pygame

scoredict = {
    0: 'zero.png',
    1: 'one.png',
    2: 'two.png',
    3: 'three.png',
    4: 'four.png',
    5: 'five.png',
    6: 'six.png',
    7: 'seven.png',
    8: 'eight.png',
    9: 'nine.png'
}

scoreimage = scoredict[leftPoints]


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(scoredict[leftPoints])
        self.rect = self.image.get_rect()


