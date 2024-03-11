#!/bin/python3

import pygame 

#create canvas
G_height, G_width = 700, 700
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((G_height,G_width))
#title
pygame.display.set_caption("Tennis")

#PLAYER SETUP
class player1:
    def __init__(self, x, y, xS, yS):
        self.x = x
        self.y = y
        self.xS = xS
        self.yS = yS
        self.yVel = 0
        self.rect = pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.xS, self.yS))
        self.score = 0

    def draw(self):
        if self.yVel+self.y > 0 and self.yVel+self.y < G_height-self.yS:
            self.y+=self.yVel
            self.rect = pygame.draw.rect(screen, (255,0,0),(self.x, self.y, self.xS, self.yS))

        else:
            self.yVel = 0
            self.rect = pygame.draw.rect(screen, (0,0,255) ,(self.x, self.y, self.xS, self.yS))


P1 = player1(0, 250, 10, 50)

class player2:
    def __init__(self, x, y, xS, yS):
        self.x = x
        self.y = y
        self.xS = xS
        self.yS = yS
        self.yVel = 0
        self.rect = pygame.draw.rect(screen, (0,0,255), (self.x, self.y, self.xS, self.yS))
        self.score = 0

    def draw(self):
        if self.yVel+self.y > 0:
            self.y+=self.yVel
            self.rect = pygame.draw.rect(screen, (0,0,255) ,(self.x, self.y, self.xS, self.yS))

        else:
            self.yvel = 0
            self.rect = pygame.draw.rect(screen, (0,0,255) ,(self.x, self.y, self.xs, self.ys))

P2 = player1(G_width-10, 250, 10, 50)


class BALL:
    def __init__(self, x, y, Xs, Ys):
        self.x = x
        self.y = y
        self.Xs = 10
        self.Ys = 10
        self.Xvel = 5
        self.Yvel = 3
        self.rect = pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.Xs, self.Ys))

    def draw(self):
        self.x += self.Xvel
        self.y += self.Yvel
        #CHECK IF WON

        #HIT TOP/BOTTOM OF SCREEN
        if self.y <= 0 or self.y > G_height-self.Ys:
            self.Yvel *= -1

        #HIT A PLAYER
        elif self.rect.colliderect(P2.rect) or self.rect.colliderect(P1.rect):
            if self.x-50 < 0:
                self.x += 10
            else:
                self.x -= 10
            self.Xvel *= -1

        self.rect = pygame.draw.rect(screen, (255,255,255) ,(self.x, self.y, self.Xs, self.Ys))

ball = BALL(G_width/2 ,G_height/2 ,10,10)


def updateScreen(running):
    P1.draw()
    P2.draw()
    ball.draw()

    #middle line
    pygame.draw.rect(screen, (30,30,30), (G_width/2,0, 5, G_height))

    #SCORE DISPLAY STUFF
    if running:
        if P1.score == 15:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("PLAYER 1 WON!", True, (255,255,255), (108,147,92))
            textRect = text.get_rect()

            textRect.center = (G_width//2, G_height//2)
            screen.blit(text, textRect)
            running = False
            return running
        elif P2.score == 15:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("PLAYER 2 WON!", True, (255,255,255), (108,147,92))
            textRect = text.get_rect()

            textRect.center = (G_width//2, G_height//2)
            screen.blit(text, textRect)
            running = False
            return running
        else:
            font = pygame.font.Font('freesansbold.ttf', 32)

            text = font.render("1: "+str(P1.score)+"|2: "+str(P2.score), True, (255,255,255), (108,147,92))
            textRect = text.get_rect()

            textRect.center = (G_width//2, G_height//2)
            screen.blit(text, textRect)
            running=True
            return running

def checkWin(ball, P1, P2):
    won = False
    if ball.x < 0:
        P2.score += 1
        won = True

    elif ball.x > G_width:
        P1.score += 1
        won = True

    if won:
        ball.x = G_width/2
        ball.y = G_height/2
        won=False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #INPUT FOR MOVEMENT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                P2.yVel += 6
            elif event.key == pygame.K_UP:
                P2.yVel -= 6
            elif event.key == pygame.K_w:
                P1.yVel -= 6
            elif event.key == pygame.K_s:
                P1.yVel += 6
            elif event.key == pygame.K_SPACE:
                running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                P2.yVel = 0
            elif event.key == pygame.K_UP:
                P2.yVel = 0
            elif event.key == pygame.K_w:
                P1.yVel = 0
            elif event.key == pygame.K_s:
                P1.yVel = 0

    screen.fill((108,147,92))
    checkWin(ball, P1, P2)
    running = updateScreen(running)
    pygame.display.update()
    clock.tick(60)
