import pygame
import random
import math

#initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((900, 600))

# load background image
background = pygame.image.load("arena.jpg")
background = pygame.transform.scale(background, (900, 600))   # resize image

# title and icon
pygame.display.set_caption("Tournament of Champions")
icon = pygame.image.load("roman-helmet.png")
pygame.display.set_icon(icon)

# load player image
player_img = pygame.image.load("wizard.png")
player_img = pygame.transform.scale(player_img, (64, 64))   # resize image

fireball_img = pygame.image.load("fireball.png")
fireball_img = pygame.transform.scale(fireball_img, (32,32))    #resize!

snowball_img = pygame.image.load("snowball.png")
snowball_img = pygame.transform.scale(snowball_img, (32, 32))   #resize!

enemy_img = pygame.image.load("devil.png")
enemy_img = pygame.transform.scale(enemy_img, (48, 48))   # resize image

# define player initial placement and score
player_score = 0
x_cor = 200
y_cor = 50
x_change = 0
y_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

# define fireball initial placement
fireball_x_cor = 50
fireball_y_cor = 200
fireball_x_change = 0.2
fireball_y_change = 0
fireball_state = "ready"
def fireball(x, y):
    screen.blit(fireball_img, (x, y))
def fire_fireball(x, y):
    # x,y coordinates changed in order to seem like fireball apears from wizard hand
    x += 10
    y += 25
    global fireball_state
    global fireball_engaged

    fireball_state = "fire"
    screen.blit(fireball_img, (x, y))

# define snowball initial placement
snowball_x_cor = 50
snowball_y_cor = 200
snowball_x_change = 0.2
snowball_y_change = 0
snowball_state = "ready"
def snowball(x, y):
    screen.blit(snowball_img, (x, y))
def fire_snowball(x, y):
    # x,y coordinates changed in order to seem like snowball apears from wizard hand
    x += 10
    y += 25
    global snowball_state

    snowball_state = "fire"
    screen.blit(snowball_img, (x, y))

#define collision
def isCollision(enemyX, enemyY, fireballX, fireballY):
    #using equation to calculate distance between two points
    fireballX -= 5
    D = math.sqrt(math.pow((enemyX - fireballX),2) + (math.pow((enemyY - fireballY),2)))

    if D < 27:
        return True
    else:
        return False

# define enemy initial placement
enemy_start_x = random.randint(65, 835)
enemy_x_cor = enemy_start_x
enemy_y_cor = random.randint(65, 535)
enemy_x_change = 0
enemy_x_change += 0.025
enemy_y_change = 0
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# game loop
running = True
while running:

    # fill screen R,G,B
    screen.fill((1,255,0))

    # fill screen with image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # check window exit
        if event.type == pygame.QUIT:
            running = False
        # check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 0.3
            if event.key == pygame.K_RIGHT:
                x_change += 0.3

            if event.key == pygame.K_DOWN:
                y_change += 0.3
            if event.key == pygame.K_UP:
                y_change -= 0.3
            
            if event.key == pygame.K_SPACE:
                if fireball_state == "ready":    
                    fireball_x_cor = x_cor
                    fireball_y_cor = y_cor
                    fire_fireball(fireball_x_cor, fireball_y_cor)
            
            if event.key == pygame.K_s:
                if snowball_state == "ready":    
                    snowball_x_cor = x_cor
                    snowball_y_cor = y_cor
                    fire_snowball(snowball_x_cor, snowball_y_cor)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
    
    # player coordinate changes
    x_cor += x_change
    y_cor += y_change

    # player boundries
    if y_cor <= 0:
        y_cor = 0
    elif y_cor >= 536:
        y_cor = 536
    
    if x_cor <= 0:
        x_cor = 0
    elif x_cor >= 836:
        x_cor = 836

    # fireball movement
    if fireball_x_cor > 900:
        fireball_x_cor = x_cor
        fireball_y_cor = y_cor
        fireball_state = "ready"

    if fireball_state == "fire":
        fire_fireball(fireball_x_cor, fireball_y_cor)
        fireball_x_cor += fireball_x_change

    # snowball movement
    if snowball_x_cor > 900:
        snowball_x_cor = x_cor
        snowball_y_cor = y_cor
        snowball_state = "ready"

    if snowball_state == "fire":
        fire_snowball(snowball_x_cor, snowball_y_cor)
        snowball_x_cor += snowball_x_change

    # enemy coordinate changes
    enemy_x_cor += enemy_x_change
    #enemy_y_cor += enemy_y_change

    # enemy window boundries
    if enemy_y_cor <= 0:
        enemy_y_cor = 0
    elif enemy_y_cor >= 552:
        enemy_y_cor = 552
    
    if enemy_x_cor <= 0:
        enemy_x_cor = 0
    elif enemy_x_cor >= 852:
        enemy_x_cor = 852

    # enemy movement boundries
    if enemy_x_cor > (enemy_start_x + 25):
        enemy_x_change -= 0.025
    elif enemy_x_cor < (enemy_start_x - 25):
        enemy_x_change += 0.025

    # check if fireball has collided with enemy
    if isCollision(enemy_x_cor, enemy_y_cor, fireball_x_cor, fireball_y_cor):
        # reset fireball
        fireball_x_cor = x_cor
        fireball_y_cor = y_cor
        fireball_state = "ready"
        # reset enemy
        enemy_start_x = random.randint(65, 835)
        enemy_x_cor = enemy_start_x
        enemy_y_cor = random.randint(65, 535)
        # update score
        player_score += 1
        print(player_score)

    
    
    player(x_cor,y_cor)
    enemy(enemy_x_cor, enemy_y_cor)
    pygame.display.update()
