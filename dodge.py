import pygame
import sys
import random

#initialize pygame
pygame.init()
pygame.display.set_caption("Donald Trump Dodge") # Title for the app
width = 800
height = 600
my_color = (50, 200, 20)
black = (0,0,0)
player_size = 50
enemy_size = 30
player_pos = [width / 2, height - 2 * player_size]
enemy_pos = [random.randint(0, width - enemy_size), 0]
blue = (0, 50, 240)
step = 20
speed = 0
enemy_list = [enemy_pos]
score = 0
myFont = pygame.font.SysFont("monospace", 35)
yellow = (255, 255, 0)
animCount = 0
left = False
right = False
# initialize a display with given width and heigth
display = pygame.display.set_mode((width, height))
game_over = False
clock = pygame.time.Clock()

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.2:
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(display, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for index, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] <= height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(index)
            score += 10
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def set_level(score, speed):
    if score < 200:
        speed = 3
    elif score < 400:
        speed = 5
    elif score < 600:
        speed = 8
    elif score < 1000:
        speed = 10
    elif speed < 1500:
        speed = 15
    elif speed < 1800:
        speed = 20
    elif speed < 2000:
        speed = 25
    elif speed < 2500:
        speed = 30
    elif speed < 3000:
        speed = 37
    elif speef < 3500:
        speed = 45
    else:
        speed = 50
    return speed

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


walkRight = [pygame.image.load('sprites/pygame_right_1.png'),
             pygame.image.load('sprites/pygame_right_2.png'),
             pygame.image.load('sprites/pygame_right_3.png'),
             pygame.image.load('sprites/pygame_right_4.png'),
             pygame.image.load('sprites/pygame_right_5.png'),
             pygame.image.load('sprites/pygame_right_6.png')]
walkLeft = [pygame.image.load('sprites/pygame_left_1.png'),
            pygame.image.load('sprites/pygame_left_2.png'),
            pygame.image.load('sprites/pygame_left_3.png'),
            pygame.image.load('sprites/pygame_left_4.png'),
            pygame.image.load('sprites/pygame_left_5.png'),
            pygame.image.load('sprites/pygame_left_6.png')]
playerStand = pygame.image.load('sprites/idle.png')
#bg = pygame.image.load('sprites/pygame_bg.jpg')
playerStand = pygame.image.load('sprites/idle.png')

def drawDisplay():
    global animCount

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        display.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        display.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        display.blit(playerStand, (x, y))

    pygame.display.update()


# Infinite loop, running while the game is played
while not game_over:

    #The for looop, getting the events
    for event in pygame.event.get():

        #now i can exit by exiting the program as a window
        if event.type == pygame.QUIT:
            sys.exit()

    x = player_pos[0]
    y = player_pos[1]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        x -= step
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and player_pos[0] < (width - player_size):
        x += step
        right = True
        left = False
    else:
        left = False
        right = False


    player_pos = [x, y]

    display.fill(black)

    #update position of the enemy

    if detect_collision(player_pos, enemy_pos) == True:
        game_over = True

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    speed = set_level(score, speed)
    text = "Score:" + str(score)
    label = myFont.render(text, 1, yellow)
    display.blit(label, (width - 200, height - 40))
    if collision_check(enemy_list, player_pos):
        game_over = True
        print('You lose!')
    draw_enemies(enemy_list)

    # i am drawing rectangles on each iteration
    #pygame.draw.rect(display, my_color, (player_pos[0], player_pos[1], player_size, player_size))
    drawDisplay()
    clock.tick(30)

    pygame.display.update()
