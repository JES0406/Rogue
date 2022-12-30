import pygame, math, random
from constantes import *
pygame.init()


print('Espacio para hacer que aparezca un enemigo al azar')
### Player variables
pwidth = 32
pheight = 32
playerpos = [20, 20]
pspeed = 5
mov_r = False
mov_l = False
mov_u = False
mov_d = False

def setspeed(): ### Si el jugador se desplaza a la vez en los ejes x e y, tiene que moverse más lento en ambos ejes (si no su velocidad total es considerablemente mayor)
    movingdirections = 0
    for element in [mov_l, mov_r, mov_u, mov_d]:
        if element: movingdirections += 1
    if movingdirections > 1: movespeed = (2*pspeed)**1/2
    else: movespeed = pspeed
    return int(movespeed)



enemy_list = []
enemy_id = 0
class enemy:
    def __init__(self, speed, range, position:tuple, type):
        self.type = type
        self.speed = speed
        self.range = range + pwidth
        self.position = [position[0], position[1]]
        global enemy_id
        self.id = enemy_id
        enemy_id += 1
        
    def move(self, target:list):
            ### Ranged enemy movement
        distance_x = target[0] - self.position[0]
        distance_y = target[1] - self.position[1]
        distance = math.sqrt(distance_x**2 + distance_y **2)
        if distance < self.range: 
            ranged_espeed_vector = -self.speed
        elif abs(distance - self.range) < self.speed: ranged_espeed_vector = 0 
        else: ranged_espeed_vector = self.speed
        if self.position[0] < self.speed + target[0]: self.position[0] += ranged_espeed_vector
        elif self.position[0] > self.speed + target[0]: self.position[0] -= ranged_espeed_vector
        if self.position[1] < self.speed + target[1]: self.position[1] += ranged_espeed_vector
        elif self.position[1] > self.speed + target[1]: self.position[1] -= ranged_espeed_vector




def addenemy(which:int):
    global enemy_list
    if which == 0: enemy_list.append(enemy(speed = 2.5, range = 20, position = (random.randint(0, ANCHO - pwidth), random.randint(0, ALTO- pheight)), type = which))
    if which == 1: enemy_list.append(enemy(speed = 2.5, range = 200, position = (random.randint(0, ANCHO - pwidth), random.randint(0, ALTO- pheight)), type = which))

    
### Screen
bgcolor = color_black
pygame.display.set_caption('game.py')
color_list = [color_red, color_white]

### Main loop
run = True
while run:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False

        ### Start moving here
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: mov_l = True
            if event.key == pygame.K_RIGHT: mov_r = True
            if event.key == pygame.K_UP: mov_u = True
            if event.key == pygame.K_DOWN: mov_d = True
            if event.key == pygame.K_SPACE:
                addenemy(random.randint(0,1))
                print(len(enemy_list))
            if event.key == pygame.K_TAB:
                for i in range(300):
                    addenemy(random.randint(0,1))
                    print(len(enemy_list))

        ### Stop moving here
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mov_l = False
            if event.key == pygame.K_RIGHT:
                mov_r = False
            if event.key == pygame.K_UP:
                mov_u = False
            if event.key == pygame.K_DOWN:
                mov_d = False

    moving_speed = setspeed()
    ### Actual movement of the player
    if mov_l and playerpos[0] > 0: playerpos[0] -= moving_speed
    if mov_r and playerpos [0] < ANCHO - pwidth: playerpos[0] += moving_speed
    if mov_u and playerpos[1] > 0: playerpos[1] -= moving_speed
    if mov_d and playerpos[1] < ALTO - pheight: playerpos[1] += moving_speed


    pygame.draw.rect(screen, color_green, pygame.Rect(playerpos[0], playerpos[1], pwidth, pheight), width = 0)
    for bad_guy in enemy_list: 
        bad_guy.move(playerpos)
        pygame.draw.rect(screen, color_list[bad_guy.type], pygame.Rect(bad_guy.position[0], bad_guy.position[1], pwidth, pheight), width = 0)

    #pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
