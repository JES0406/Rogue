import pygame, math, random
from constantes import *
pygame.init()

print('Espacio para hacer que aparezca un enemigo al azar')
### Player variables
pwidth = 32
pheight = 32
playerpos = [ANCHO / 2, ALTO / 2]
pspeed = 5
pdamage = 7
player_melee_range = 50
phealth = 10
def check_if_player_is_dead():
    if phealth <= 0: print('YOU DIED')
mov_r = False
mov_l = False
mov_u = False
mov_d = False

### Map and camera
mapwidth = 2 * ANCHO
mapheight = 2 * ALTO
camera_left_top = [0,0]

def get_camera_centre(): return (camera_left_top[0] + ANCHO/2, camera_left_top[1] + ALTO/2)

def update_camera_pos():
    global camera_left_top
    camera_left_top[0] = min(max(0, playerpos[0] - (ANCHO / 2)), mapwidth - ANCHO)
    camera_left_top[1] = min(max(0, playerpos[1] - (ALTO / 2)), mapheight - ALTO)

def relative_pos(position, coordinate:int) -> int: 
    return position[coordinate] - camera_left_top[coordinate]

def draw_minimap():
    pygame.draw.rect(screen, 'White', pygame.Rect(0,0,ANCHO / 4 + 2, ALTO / 4 +2))
    pygame.draw.rect(screen, 'Black', pygame.Rect(0,0,ANCHO / 4, ALTO / 4))
    pygame.draw.rect(screen, color_green, pygame.Rect(playerpos[0]/8,playerpos[1]/8,pheight/8, pheight/8))
    for enemy in enemy_list:
        pygame.draw.rect(screen, color_list[enemy.type], pygame.Rect(enemy.position[0]/8,enemy.position[1]/8,pheight/8, pheight/8))


def setspeed(): ### Si el jugador se desplaza a la vez en los ejes x e y, tiene que moverse más lento en ambos ejes (si no su velocidad total es considerablemente mayor)
    movingdirections = 0
    for element in [mov_l, mov_r, mov_u, mov_d]:
        if element: movingdirections += 1
    if movingdirections > 1: movespeed = (2*pspeed)**1/2
    else: movespeed = pspeed
    return int(movespeed)

def calc_distance(point_A:list, point_B:list) -> float:
    distance_x = point_A[0] - point_B[0]
    distance_y = point_A[1] - point_B[1]
    distance = math.sqrt(distance_x**2 + distance_y **2)
    return distance



enemy_list = []
enemy_id = 0
class Enemy:
    def __init__(self, speed, range, position:tuple, type, hp = 20, attack_cooldown = 60, damage = 5):
        self.type, self.speed, self.range, self.position, self.hp, self.dmg = type, speed, range + pwidth, list(position), hp, damage
        self.attack_timer = 0
        self.attack_cooldown = attack_cooldown
        enemy_list.append(self)
        
    def shoot(self):
        target = [playerpos[0] + pheight/2, playerpos[1] + pheight/2]
        Projectile(self.position, target, 4, 2, self.dmg, False, False)
    def melee(self):
        global phealth
        if calc_distance(playerpos, self.position) <= self.range + 10:
            pygame.draw.circle(screen, 'Red', (relative_pos(self.position, 0)+1/2*pheight\
                , relative_pos(self.position, 1)+1/2*pheight), self.range+10, 10)
            phealth -= self.dmg
            print(phealth)
            check_if_player_is_dead()
    def attack(self):
        if self.type == 1: self.shoot()
        elif self.type == 0: self.melee()

    def pathfind_and_update(self, target:list):
        #pathfind
        distance = calc_distance(target, self.position)
        if distance < self.range: 
            speed_vector = -self.speed
        elif abs(distance - self.range) < self.speed *2 : speed_vector = 0 
        else: speed_vector = self.speed
        if self.position[0] < self.speed + target[0]: self.position[0] += speed_vector
        elif self.position[0] > self.speed + target[0]: self.position[0] -= speed_vector
        if self.position[1] < self.speed + target[1]: self.position[1] += speed_vector
        elif self.position[1] > self.speed + target[1]: self.position[1] -= speed_vector
        #update
        self.attack_timer += 1
        if self.attack_timer >= self.attack_cooldown:
            self.attack_timer = 0
            self.attack()

    def damage(self, hp_loss):
        self.hp -= hp_loss
        if self.hp <= 0:
            enemy_list.remove(self)
    
projectile_list = []
class Projectile:
    def __init__(self, position:list, target_position, size: int, speed: int, damage: int, piercing: bool, player_team:bool):
        self.position = [position[0], position[1]] # Hay que hacerlo así porque si no, solo se crea un pointer a la pos. del jugador
        self.size, self.damage, self.piercing, self.player_team = size, damage, piercing, player_team
        self.speed_x = speed * (target_position[0]-position[0])/max(calc_distance(self.position, target_position),0.001)
        self.speed_y = speed * (target_position[1]-position[1])/max(calc_distance(self.position, target_position),0.001)
        projectile_list.append(self)
    def update(self):
        global phealth
        hit_target = False
        if self.player_team:
            for enemy in enemy_list:
                if enemy.position[0] < self.position[0] < enemy.position[0] + pheight:
                    if enemy.position[1] < self.position[1] < enemy.position[1] + pheight:
                        enemy.damage(self.damage)
                        hit_target = True
        else: 
            if playerpos[0] < self.position[0] < playerpos[0] + pheight:
                if playerpos[1] < self.position[1] < playerpos[1] + pheight:
                    phealth -= self.damage
                    hit_target = True
                    print(phealth)
                    check_if_player_is_dead()
        self.position[0] += self.speed_x
        self.position[1] += self.speed_y
        pygame.draw.circle(screen, 'White', (relative_pos(self.position, 0), relative_pos(self.position, 1)), self.size)
        if not (0 < self.position[0] < mapwidth) or not (0 < self.position[1] < mapheight):
            self.piercing, hit_target = False, True
        if hit_target and not self.piercing:
            projectile_list.remove(self)




def addenemy(which:int):
    global enemy_list
    if which == 0: Enemy(speed = 2.5, range = 20, position = (random.randint(0, mapwidth - pwidth), random.randint(0, mapheight- pheight)), type = which)
    if which == 1: Enemy(speed = 2.5, range = 200, position = (random.randint(0, mapwidth - pwidth), random.randint(0, mapheight- pheight)), type = which)
    if which == 2: Enemy(speed = 0, range = 0, position = (random.randint(0, mapwidth - pwidth), random.randint(0, mapheight- pheight)), type = which)

    
### Screen
bgcolor = color_black
pygame.display.set_caption('game.py')
color_list = [color_red, color_white, 'Orange']

### Main loop
run = True
while run:
    update_camera_pos()
    screen.fill(bgcolor)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False

        ### Start moving here
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: mov_l = True
            elif event.key == pygame.K_d: mov_r = True
            elif event.key == pygame.K_w: mov_u = True
            elif event.key == pygame.K_s: mov_d = True
            elif event.key == pygame.K_e: 
                target = (pygame.mouse.get_pos()[0] + camera_left_top[0], pygame.mouse.get_pos()[1] + camera_left_top[1])
                Projectile(playerpos, target, 10, 20, pdamage, False, True)
            elif event.key == pygame.K_q:
                target = (pygame.mouse.get_pos()[0] + camera_left_top[0], pygame.mouse.get_pos()[1] + camera_left_top[1])
                pygame.draw.circle(screen, 'Blue', (relative_pos(playerpos, 0)+1/2*pheight\
                , relative_pos(playerpos, 1)+1/2*pheight), player_melee_range + pheight, 10)
                for enemy in enemy_list:
                    if calc_distance(playerpos, enemy.position) <= player_melee_range + pheight:
                        enemy.damage(pdamage)
            elif event.key == pygame.K_SPACE:
                addenemy(random.randint(0,2))
                print(len(enemy_list))
            elif event.key == pygame.K_TAB:
                for i in range(300):
                    addenemy(random.randint(0,2))
                    print(len(enemy_list))

        ### Stop moving here
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mov_l = False
            elif event.key == pygame.K_d:
                mov_r = False
            elif event.key == pygame.K_w:
                mov_u = False
            elif event.key == pygame.K_s:
                mov_d = False

    moving_speed = setspeed()
    ### Actual movement of the player
    if mov_l and playerpos[0] > 0: playerpos[0] -= moving_speed
    elif mov_r and playerpos [0] < mapwidth - pwidth: playerpos[0] += moving_speed
    if mov_u and playerpos[1] > 0: playerpos[1] -= moving_speed
    elif mov_d and playerpos[1] < mapheight - pheight: playerpos[1] += moving_speed


    pygame.draw.rect(screen, color_green, pygame.Rect(relative_pos(playerpos, 0), relative_pos(playerpos, 1), pwidth, pheight), width = 0)
    for bad_guy in enemy_list: 
        bad_guy.pathfind_and_update(playerpos)
        pygame.draw.rect(screen, color_list[bad_guy.type],\
             pygame.Rect(relative_pos(bad_guy.position, 0), relative_pos(bad_guy.position, 1), pwidth, pheight), width = 0)
    for projectile in projectile_list:
        projectile.update()

    #pygame.display.update()
    draw_minimap()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()