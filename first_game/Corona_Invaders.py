
import pygame
import random
import math
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.init()

from pygame import mixer

# Screen size, game caption and game icon
screen = pygame.display.set_mode((880, 680))
pygame.display.set_caption("Corona Invaders")
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)


# Game backround
backround = pygame.image.load("6870.jpg") 
backroundX = 0
backroundY = 0

# Backround music
mixer.music.load("bensound-evolution.mp3")
mixer.music.play(-1)


# Goal
goal = pygame.image.load("objective.png")
goalX = float(440)
goalY = float(0)

# Player
player = pygame.image.load("coronavirus.png")
playerX = float(440)
playerY = float(550)
playerX_move = 0
playerY_move = 0

# Enemies
enemy = pygame.image.load("boss3.png")

enemyX = random.randint(0, 880)
enemyY = float(100)
enemyX_move = 8 
enemyY_move = 0

enemy2 = pygame.image.load("boss2.png")
enemy2X = random.randint(0, 880)
enemy2Y = float(200)
enemy2X_move = 10 
enemy2Y_move = 0

enemy3 = pygame.image.load("boss1.png")
enemy3X = random.randint(0, 880)
enemy3Y = float(300)
enemy3X_move = 10 
enemy3Y_move = 0

enemy4 = pygame.image.load("boss4.png")
enemy4X = random.randint(0, 880)
enemy4Y = float(450)
enemy4X_move = 5
enemy4Y_move = 0

def iscollision_G(goalX, goalY, playerX, playerY):
    distance = math.sqrt((goalX - playerX)**2 + (goalY - playerY)**2)
    if distance < 45:
        return True
    else:
        return False

def iscollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((enemyX - playerX)**2 + (enemyY - playerY)**2)
    if distance < 45:
        return True
    else:
        return False

def iscollision_2(enemy2X, enemy2Y, playerX, playerY):
    distance = math.sqrt((enemy2X - playerX)**2 + (enemy2Y - playerY)**2)
    if distance < 45:
        return True
    else:
        return False

def iscollision_3(enemy3X, enemy3Y, playerX, playerY):
    distance = math.sqrt((enemy3X - playerX)**2 + (enemy3Y - playerY)**2)
    if distance < 45:
        return True
    else:
        return False

def iscollision_4(enemy4X, enemy4Y, playerX, playerY):
    distance = math.sqrt((enemy4X - playerX)**2 + (enemy4Y - playerY)**2)
    if distance < 45:
        return True
    else:
        return False
    

run = True
while run:
    
    screen.fill((137, 96, 167))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move = -4
            if event.key == pygame.K_RIGHT:
                playerX_move = 4
            if event.key == pygame.K_UP:
                playerY_move = -4
            if event.key == pygame.K_DOWN:
                playerY_move = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_move = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_move = 0
                
    playerX += playerX_move
    playerY += playerY_move

    if playerX <= 0:
        playerX = 0
    elif playerX >= 815:
        playerX = 815

    if playerY <= 0:
        playerY = 0
    elif playerY >= 615:
        playerY = 615

    enemyX += enemyX_move

    if enemyX <= 0:
        enemyX_move = 8
    elif enemyX >= 815:
        enemyX_move = - 8

    enemy2X += enemy2X_move

    if enemy2X <= 0:
        enemy2X_move = 10
    elif enemy2X >= 815:
        enemy2X_move = - 10

    enemy3X += enemy3X_move

    if enemy3X <= 0:
        enemy3X_move = 10
    elif enemy3X >= 815:
        enemy3X_move = - 10

    enemy4X += enemy4X_move

    if enemy4X <= 0:
        enemy4X_move = 5
    elif enemy4X >= 815:
        enemy4X_move = - 5

    collision = iscollision_G(goalX,goalY,playerX,playerY) 
    if collision:
        die_sound = mixer.Sound("applause2.wav")
        die_sound.play()
        print("You Win!")
        exit(0)
    collision = iscollision(enemyX,enemyY,playerX,playerY) 
    if collision:
        die_sound = mixer.Sound("wickedwitchlaugh.wav")
        die_sound.play()
        print("You loose")
        exit(0)

    collision = iscollision_2(enemy2X,enemy2Y,playerX,playerY) 
    if collision:
        die_sound = mixer.Sound("wickedmalelaugh1.wav")
        die_sound.play()
        print("You loose")
        exit(0)

    collision = iscollision_3(enemy3X,enemy3Y,playerX,playerY) 
    if collision:
        die_sound = mixer.Sound("Laugh+2.wav")
        die_sound.play()
        print("You loose")
        exit(0)

    collision = iscollision_4(enemy4X,enemy4Y,playerX,playerY) 
    if collision:
        die_sound = mixer.Sound("wickedwitchlaugh.wav")
        die_sound.play()
        print("You loose")
        exit(0)

        
    screen.blit(backround,(backroundX, backroundY))    
    screen.blit(goal, (goalX, goalY))
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    screen.blit(enemy2, (enemy2X, enemy2Y))
    screen.blit(enemy3, (enemy3X, enemy3Y))
    screen.blit(enemy4, (enemy4X, enemy4Y))
    pygame.display.flip()

    pygame.display.update()

