import pygame
from paddle import Paddle
from ball import Ball
from random import randint
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong")

leftPoints = 0
rightPoints = 0

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
    9: 'nine.png',
    10: 'nine.png'
}


class leftScoreSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(scoredict[leftPoints])
        self.rect = self.image.get_rect()
    def update(self):
        self.image = pygame.image.load(scoredict[leftPoints])


class rightScoreSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(scoredict[rightPoints])
        self.rect = self.image.get_rect()
    def update(self):
        self.image = pygame.image.load(scoredict[rightPoints])

all_sprites_list = pygame.sprite.Group()

leftPaddle = Paddle(white, 5, 80)
leftPaddle.rect.x = 10
leftPaddle.rect.y = 10

rightPaddle = Paddle(white, 5, 80)
rightPaddle.rect.x = 585
rightPaddle.rect.y = 10

leftScore = leftScoreSprite()
leftScore.rect.x = 271
leftScore.rect.y = 10

rightScore = rightScoreSprite()
rightScore.rect.x = 314
rightScore.rect.y = 10



ball = Ball(white, 8, 8)
ball.rect.x = 298
ball.rect.y = 198

all_sprites_list.add(leftPaddle)
all_sprites_list.add(rightPaddle)
all_sprites_list.add(ball)
all_sprites_list.add(leftScore)
all_sprites_list.add(rightScore)


def ballreset():
    ball.rect.x = 298
    ball.rect.y = 198


keepRunning = True
titleScreen = True
cursorloc = 1
clock = pygame.time.Clock()
helpScreen = False


while titleScreen:
    title1 = pygame.image.load('title1.png')
    title2 = pygame.image.load('title2.png')
    title3 = pygame.image.load('title3.png')
    help = pygame.image.load('help.png')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titleScreen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if cursorloc >= 1:
                    cursorloc -= 1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if cursorloc <= 3:
                    cursorloc += 1
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if helpScreen:
                    helpScreen = False
                elif cursorloc == 1:
                    titleScreen = False
                elif cursorloc == 2:
                    helpScreen = True
                elif cursorloc == 3:
                    pygame.quit()
    if not helpScreen:
        if cursorloc == 1:
            screen.blit(title1, (0,0))
        elif cursorloc == 2:
            screen.blit(title2, (0,0))
        elif cursorloc == 3:
            screen.blit(title3, (0,0))
    elif helpScreen:
        screen.blit(help, (0,0))

    pygame.display.flip()
    clock.tick(60)

served = False


def randspeeds():
    global vertSpeed, leftorRight
    vertSpeed = randint(-5, 5)
    leftorRight = randint(1, 2)


vertSpeed = 0
horizSpeed = 0
leftorRight = 0

while keepRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        keepRunning = False
    if keys[pygame.K_w] and leftPaddle.rect.y > 0:
        leftPaddle.moveup(7)
    if keys[pygame.K_s] and leftPaddle.rect.y < 325:
        leftPaddle.movedown(7)
    if keys[pygame.K_UP] and rightPaddle.rect.y > 0:
        rightPaddle.moveup(7)
    if keys[pygame.K_DOWN] and rightPaddle.rect.y < 325:
        rightPaddle.movedown(7)
    if keys[pygame.K_SPACE] and not served:
        served = True
        randspeeds()
        if leftorRight == 1:
            horizSpeed = -5
        if leftorRight == 2:
            horizSpeed = 5
    if served:
        ball.moveHoriz(horizSpeed)
        ball.moveVert(vertSpeed)
        if ball.rect.x <= 1:
            served = False
            rightPoints += 1
            rightScoreSprite.update
            ballreset()
        elif ball.rect.x >= 594:
            served = False
            leftPoints += 1
            leftScoreSprite.update
            ballreset()
        elif ball.rect.y <= 1 or ball.rect.y >= 395:
            vertSpeed *= -1
        if ball.is_collided_with(leftPaddle) or ball.is_collided_with(rightPaddle):
            horizSpeed *= -1
            vertSpeed = randint(-10, 10)
        if leftPoints == 10 or rightPoints == 10:
            keepRunning = False

    screen.fill(black)
    pygame.draw.rect(screen, white, [296, 18, 8, 4], 0)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(73)