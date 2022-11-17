import pygame, math
pygame.init



### Player variables
pwidth = 15
pheight = 15
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

## Enemy variables
melee_epos = [200, 200]
melee_espeed = 2.5
melee_range = 20

ranged_epos = [400, 100]
ranged_espeed = 1.5
kiting_distance = 200 ### Distancia a la que se quedan los enemigos con rango del jugador

### Clock
fps = 60
fpsclock = pygame.time.Clock()

###Colours
color_white = '#fcfaf9'
color_black = '#333333'
color_green = '#48E5C2'
color_red = '#ce5e5e'

### Screen
swidth = 600
sheight = 600
bgcolor = color_black
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('game.py')


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
    if mov_r and playerpos [0] < swidth - pwidth: playerpos[0] += moving_speed
    if mov_u and playerpos[1] > 0: playerpos[1] -= moving_speed
    if mov_d and playerpos[1] < sheight - pheight: playerpos[1] += moving_speed

    ### Melee enemy movement
    if melee_epos[0] + melee_range < playerpos[0]: melee_epos[0] += melee_espeed
    elif melee_epos[0] - melee_range > playerpos[0]: melee_epos[0] -= melee_espeed
    if melee_epos[1] + melee_range < playerpos[1]: melee_epos[1] += melee_espeed
    elif melee_epos[1] -melee_range > playerpos[1]: melee_epos[1] -= melee_espeed

    ### Ranged enemy movement
    distance_x = playerpos[0] - ranged_epos[0]
    distance_y = playerpos[1] - ranged_epos[1]
    distance = math.sqrt(distance_x**2 + distance_y **2)
    if distance < kiting_distance: 
        ranged_espeed_vector = -ranged_espeed
    elif abs(distance - kiting_distance) < ranged_espeed: ranged_espeed_vector = 0 
    else: ranged_espeed_vector = ranged_espeed
    if ranged_epos[0] < playerpos[0]: ranged_epos[0] += ranged_espeed_vector
    elif ranged_epos[0] > playerpos[0]: ranged_epos[0] -= ranged_espeed_vector
    if ranged_epos[1] < playerpos[1]: ranged_epos[1] += ranged_espeed_vector
    elif ranged_epos[1] > playerpos[1]: ranged_epos[1] -= ranged_espeed_vector

    pygame.draw.rect(screen, color_green, pygame.Rect(playerpos[0], playerpos[1], pwidth, pheight), width = 0)
    pygame.draw.rect(screen, color_red, pygame.Rect(melee_epos[0], melee_epos[1], pwidth, pheight), width = 0)
    pygame.draw.rect(screen, color_white, pygame.Rect(ranged_epos[0], ranged_epos[1], pwidth, pheight), width = 0)



    

    #pygame.display.update()
    pygame.display.flip()
    fpsclock.tick(fps)

pygame.quit()
