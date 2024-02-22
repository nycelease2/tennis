#!/bin/python3

import pygame 

player1Score = 0 
player2Score = 0


#create canvas
G_height, G_width = 500, 500
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

    def draw(self):
        if self.yVel+self.y > 0:
            self.y+=self.yVel
            self.rect = pygame.draw.rect(screen, (0,0,255) ,(self.x, self.y, self.xS, self.yS))

        else:
            self.yvel = 0
            self.rect = pygame.draw.rect(screen, (0,0,255) ,(self.x, self.y, self.xs, self.ys))

P2 = player1(490, 250, 10, 50)


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
           
ball = BALL(250,250,10,10)


def updateScreen():
    P1.draw()
    P2.draw()
    ball.draw()

def checkWin(ball, player1Score, player2Score):
    won = False
    if ball.x < 0:
        player2Score += 1
        print("Player 1: "+str(player1Score))
        print("Player 2: "+str(player2Score))
        print("\n\n\n\n")
        won = True

    elif ball.x > G_width:
        player1Score += 1
        print("Player 1: "+str(player1Score))
        print("Player 2: "+str(player2Score))
        print("\n\n\n\n")
        won = True

    if won:
        ball.x = 250
        ball.y = 250
        won=False

    return player1Score, player2Score


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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                P2.yVel = 0
            elif event.key == pygame.K_UP:
                P2.yVel = 0
            elif event.key == pygame.K_w:
                P1.yVel = 0
            elif event.key == pygame.K_s:
                P1.yVel = 0

    screen.fill((30,30,30))
    updateScreen()
    player1Score, player2Score = checkWin(ball, player1Score, player2Score)
    pygame.display.update()
    clock.tick(60)
