import math, random, pygame, sys, time, os
from constantes import *
import funciones_globales as fn

class Player(pygame.sprite.Sprite):
    def __init__(self, class_chosen):
        pygame.sprite.Sprite.__init__(self)
        self.image = fn.chosen_sprite(class_chosen, 1)
        self.animation_frame = 0
        self.sprite_moving = 'None'
        self.facing = 0
        self.attack_timer = 0
        self.position = [ANCHO//2, ALTO//2]
        self.relative_pos = [fn.relative_pos(self.position,0), fn.relative_pos(self.position,1)]
        self.rect = self.image.get_rect(center = (self.relative_pos[0], self.relative_pos[1]))
        self.size = self.image.get_size()
        self.class_chosen = class_chosen
        self.frame = 0
        if self.class_chosen == "Caballero": 
            self.attack_speed = 0.25 ## tiempo entre ataques (s)
            self.weapon = 0
            self.weapon_sprite = 'knight'
            self.speed = 4
            self.MaxHP = 100
            self.hitpoint = 10
            self.HPregen = 0.1
            self.range = 10
            self.MaxMana = 0
            self.proyectile = "slash.png"
            self.proyectile_size = 300
            self.proyectile_speed = 0
            self.death_sheet = pygame.image.load("Pixel Crawler-FREE-1.8\Heroes\Knight\Death\Death-Sheet.png").convert_alpha()
        elif self.class_chosen == "Mago": 
            self.attack_speed = 0.6 ## tiempo entre ataques (s)
            self.weapon = 1
            self.weapon_sprite = 'mage'
            self.speed = 2
            self.MaxHP = 60
            self.hitpoint = 20
            self.HPregen = 0.1
            self.range = 60
            self.MaxMana = 250
            self.proyectile = "fireball.png"
            self.proyectile_size = 30
            self.proyectile_speed = 10
            self.death_sheet = pygame.image.load("Pixel Crawler-FREE-1.8\Heroes\Wizzard\Death\Death-Sheet.png").convert_alpha()
        elif self.class_chosen == "Arquero": 
            self.attack_speed = 0.25 ## tiempo entre ataques (s)
            self.weapon = 2
            self.weapon_sprite = 'archer'
            self.speed = 6
            self.MaxHP = 40
            self.hitpoint = 20
            self.HPregen = 0.05
            self.range = 60
            self.MaxMana = 0
            self.proyectile = "arrow.png"
            self.proyectile_size = 30
            self.proyectile_speed = 10
            self.death_sheet = pygame.image.load("Pixel Crawler-FREE-1.8\Heroes\Rogue\Death\Death-Sheet.png").convert_alpha()
        elif self.class_chosen == "Curandero": 
            self.attack_speed = 0.35 ## tiempo entre ataques (s)
            self.weapon = 3
            self.weapon_sprite = 'healer'
            self.speed = 4
            self.MaxHP = 80
            self.hitpoint = 5
            self.HPregen = 0.2
            self.range = 60
            self.MaxMana = 100
            self.proyectile = "heal.png"
            self.proyectile_size = 30
            self.proyectile_speed = 2
            self.death_sheet = pygame.image.load("Pixel Crawler-FREE-1.8\Enemy\Orc Crew\Orc - Shaman\Death\Death-Sheet.png").convert_alpha()
        
        self.death_size = self.death_sheet.get_size()[0]//6
        self.Manaregen = 0.2
        self.exp = 0
        self.level = 0
        self.HP = self.MaxHP
        self.Mana = self.MaxMana
        self.exp_to_level = 100 * self.level

        
    def health_bar(self):
        '''Dibuja la barra de vida'''
        pygame.draw.rect(screen, color_red, (self.rect.x, self.rect.y - 10, self.rect.width, 5))
        pygame.draw.rect(screen, color_green, (self.rect.x, self.rect.y - 10, self.rect.width * (self.HP/self.MaxHP), 5))

    def mana_bar(self):
        '''Dibuja la barra de mana'''
        try:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))
            pygame.draw.rect(screen, color_blue, (self.rect.x, self.rect.y - 5, self.rect.width * (self.Mana/self.MaxMana), 5))
        except ZeroDivisionError:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))

    def level_up(self, choice: str):
        '''Sube de nivel
        Input: choice (str) - atributo a subir
        Output: None
        '''
        if choice == "HP":
            self.MaxHP += 10
            self.HPregen += 0.01
        elif choice == "Mana":
            self.MaxMana += 10
            self.Manaregen += 0.01
        elif choice == "Speed":
            self.speed+= 0.2
        elif choice == "Damage":
            self.hitpoint += 100
            
    def exp_bar(self):
        '''Dibuja la barra de experiencia'''
        try:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 15, self.rect.width, 5))
            pygame.draw.rect(screen, color_white, (self.rect.x, self.rect.y - 15, self.rect.width * (self.exp/self.exp_to_level), 5))
        except ZeroDivisionError:
            pygame.draw.rect(screen, color_white, (self.rect.x, self.rect.y - 15, self.rect.width, 5))
    
    def movement(self):
        '''Movimiento del jugador con teclado'''
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            mov_u = True
            self.sprite_moving = 'Right'
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            mov_d = True
            self.sprite_moving = 'Left'
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            mov_l = True
            self.sprite_moving = 'Left'
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            mov_r = True
            self.sprite_moving = 'Right'
        if not pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_LEFT]:
            mov_l = False
        if not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
            mov_r = False
        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_UP]:
            mov_u = False
        if not pygame.key.get_pressed()[pygame.K_s] and not pygame.key.get_pressed()[pygame.K_DOWN]:
            mov_d = False

        movingdirections = 0
        
        for element in [mov_l, mov_r, mov_u, mov_d]:
            if element: movingdirections += 1
        if movingdirections > 1: movespeed = (2*self.speed)**1/2
        else: movespeed = self.speed

        if mov_l and self.position[0] > 0: self.position[0] -= movespeed
        elif mov_r and self.position [0] < mapwidth - self.size[0]: self.position[0] += movespeed
        if mov_u and self.position[1] > 0: self.position[1] -= movespeed
        elif mov_d and self.position[1] < mapheight - self.size[1]: self.position[1] += movespeed

    def death_animation(self, frame: float):
        '''Animación de muerte'''
        death_frames = fn.frame_list_maker(self.death_sheet, self.death_size, color_black_1, 6)
        if frame < 6:
            self.image = death_frames[int(frame)]
            
    def update(self):
        if self.attack_timer < self.attack_speed * fps:
            self.attack_timer += 1
        if self.HP <= 0:
            self.HP = 0
            self.death_animation(int(self.frame))
            self.frame += 0.2
        else:
            if 1 + self.animation_frame//ticks_per_frame >= frames_per_animation_loop: 
                self.animation_frame = 0
            if self.sprite_moving == 'Right' or self.sprite_moving == 'Left':
                self.facing = 0
                self.animation_frame += 1
                if self.sprite_moving == 'Left': self.facing = 1
            self.sprite_moving = 'None'
            if self.facing: self.image = pygame.transform.flip(fn.chosen_sprite(self.class_chosen,1 + self.animation_frame//ticks_per_frame), True, False)
            else: self.image = fn.chosen_sprite(self.class_chosen,1 + self.animation_frame//ticks_per_frame)
            self.relative_pos = [fn.relative_pos(self.position,0), fn.relative_pos(self.position,1)]
            self.rect = self.image.get_rect(center = (self.relative_pos[0], self.relative_pos[1]))
            self.weapon_a = pygame.transform.scale(pygame.image.load(f"Graphics/Clases/new_animation/weapon_{self.weapon_sprite}.png").convert_alpha(), (40, 80))
            self.offhand_a = pygame.transform.scale(pygame.image.load(f"Graphics/Clases/new_animation/offhand_{self.weapon_sprite}.png").convert_alpha(), (40, 80))
            if pygame.mouse.get_pos()[0] < self.relative_pos[0]:
                screen.blit(self.weapon_a,(self.relative_pos[0]+15, self.relative_pos[1]-30))
                screen.blit(self.offhand_a, (self.relative_pos[0]-50, self.relative_pos[1]-30))
            else:
                self.weapon_a = pygame.transform.flip(self.weapon_a, True, False)
                self.offhand_a = pygame.transform.flip(self.offhand_a, True, False)
                screen.blit(self.weapon_a,(self.relative_pos[0]-50, self.relative_pos[1]-30))
                screen.blit(self.offhand_a, (self.relative_pos[0]+15, self.relative_pos[1]-30))
            self.health_bar()
            self.mana_bar()
            if self.HP < self.MaxHP:
                self.HP += self.HPregen
            elif self.HP > self.MaxHP:
                self.HP = self.MaxHP
            if self.Mana < self.MaxMana:
                self.Mana += self.Manaregen
            elif self.Mana > self.MaxMana:
                self.Mana = self.MaxMana
            self.exp_bar()
            self.movement()
        print(self.frame)

    
    def __str__(self) -> str:
        return f"HP: {self.HP} Mana: {self.Mana} Speed: {self.speed} Damage: {self.hitpoint} Range: {self.range} Level: {self.level}, Exp: {self.exp}"

class Button():
    def __init__(self, left_top:tuple, width_height:tuple, text = 'Menu', color1 = '#823999', color2 = '#182300', text_color = 'White'):
        placeholder = ' ' + text + ' '
        self.font = pygame.font.Font("Fuentes/Pixel/Minecraft.ttf", int((width_height[0]*1.5)//len(placeholder)))
        self.text_surface = self.font.render(placeholder, False, text_color) #text, anti aliasing, color
        self.name = text
        self.pos = left_top
        self.size = width_height
        self.color = (color1,color2)
        self.rect = pygame.Rect(left_top[0],left_top[1],width_height[0],width_height[1])

    def update(self):
        self.hovering = False
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > self.pos[0] and mousepos[0] < self.pos[0] + self.size[0]:
            if mousepos[1] > self.pos[1] and mousepos[1] < self.pos[1] + self.size[1]: self.hovering = True
        pygame.draw.rect(screen,self.color[self.hovering],self.rect, border_radius=10)
        screen.blit(self.text_surface, (self.pos[0],self.pos[1] + 20))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Graphics/Clases/new_animation/Ranged1.png").convert_alpha(), (80, 80))
        self.type = type
        self.animation_frame = 0
        if self.type == "Melee":
            self.HP = 100
            self.range = 10
            self.speed = 1
            self.hitpoint = 5
            self.attack_timer = 0
            self.attack_cooldown = 60
        elif self.type == "Ranged":
            self.HP = 50
            self.range = 100
            self.speed = 2
            self.hitpoint = 10
            self.attack_timer = 0
            self.attack_cooldown = 60
        self.position = [pos[0], pos[1]]
        self.relative_pos = [fn.relative_pos(self.position,0), fn.relative_pos(self.position,1)]
        self.rect = self.image.get_rect(center = (self.relative_pos[0], self.relative_pos[1]))
        self.size = self.image.get_size()
        self.range += self.size[0]
        
    def move(self, player: Player):
        '''Moves the enemy towards the player
        Input: Player object
        Output: None
        '''
        distance = fn.calc_distance(player.position, self.position)
        if distance < self.range: 
            speed_vector = -self.speed
        elif abs(distance - self.range) < self.speed *2 : speed_vector = 0 
        else: speed_vector = self.speed
        if distance != 0:
            self.position[0] += speed_vector * (player.position[0]-self.position[0])/(distance)
            self.position[1] += speed_vector * (player.position[1]-self.position[1])/(distance)

    def attack(self, player: Player):
        '''Shoots a projectile at the player
        Input: Player object
        Output: None
        '''
        global enemy_bullets
        if self.type == "Melee":
            if fn.calc_distance(self.relative_pos, player.relative_pos) <= self.range + self.size[0]:
                pygame.draw.line(screen, (255,0,0), self.relative_pos, player.relative_pos, 10)
                player.HP -= self.hitpoint
        elif self.type == "Ranged":
            if fn.calc_distance(self.relative_pos, player.relative_pos) <= self.range + self.size[0]:
                enemy_bullets.add(Projectile(self.position, player.position, 25, self.speed, self.hitpoint, "arrow.png"))

    def update(self, player):
        if 1 + self.animation_frame//ticks_per_frame >= frames_per_animation_loop: 
            self.animation_frame = 0
        self.animation_frame += 1
        self.relative_pos = [fn.relative_pos(self.position,0), fn.relative_pos(self.position,1)]
        self.image = pygame.transform.scale(pygame.image.load(f"Graphics/Clases/new_animation/{self.type}{1 + self.animation_frame//ticks_per_frame}.png").convert_alpha(), (80, 80))
        if player.position[0] <= self.position[0]:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center = (self.relative_pos[0], self.relative_pos[1]))
        self.move(player)
        if self.HP <= 0:
            self.kill()
            player.exp += 10
        self.attack_timer += 1
        if self.attack_timer >= self.attack_cooldown:
            self.attack_timer = 0
            self.attack(player)
            
class Projectile(pygame.sprite.Sprite):

    def __init__(self, position:list, target_position, size: int, speed: int, damage: int, weapon: str, time_to_destroy: int = 100):
        pygame.sprite.Sprite.__init__(self)
        self.position = [position[0], position[1]] # Hay que hacerlo así porque si no, solo se crea un pointer a la pos. del jugador
        self.size, self.damage, self.speed, self.weapon, self.time_to_destroy = size, damage, speed, weapon, time_to_destroy
        self.speed_x = speed * (target_position[0]-position[0])/max(fn.calc_distance(self.position, target_position),0.001)
        self.speed_y = speed * (target_position[1]-position[1])/max(fn.calc_distance(self.position, target_position),0.001)
        self.angle = math.atan2(self.speed_y, self.speed_x)
        
        self.image = pygame.transform.scale(pygame.image.load("Graphics/Clases/Proyectiles/" + weapon).convert_alpha(), (self.size, self.size))
        self.image = pygame.transform.rotate(self.image, -self.angle * 180 / math.pi)

        self.rect = self.image.get_rect(center = (self.position[0], self.position[1]))

    def update(self):

        self.relative_pos = [fn.relative_pos(self.position,0), fn.relative_pos(self.position,1)]
        self.rect = self.image.get_rect(center = (self.relative_pos[0], self.relative_pos[1]))
        self.position[0] += self.speed_x
        self.position[1] += self.speed_y
        
        if not (0 < self.position[0] < mapwidth) or not (0 < self.position[1] < mapheight):
            self.kill()
        self.time_to_destroy -= 1
        if self.time_to_destroy <= 0:
            self.kill()

class Texto(pygame.sprite.Sprite):
    def __init__(self, string, pos, size, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.string = string
        self.fuente = pygame.font.Font("Fuentes/starjedi/Starjedi.ttf", size)
        self.text = self.fuente.render(string, False, color_yellow_2)
        self.rect = self.text.get_rect(center = pos)
        self.pos = pos
        self.speed = speed
        self.size = size
    
    def change_speed(self, speed: int):
        self.speed = speed

    def update(self):
        if self.size >= 0:
            self.size = (self.pos[1])/6
            if self.size < 0:
                self.size = 0
        self.fuente = pygame.font.Font("Fuentes/starjedi/Starjedi.ttf", int(self.size))
        self.text = self.fuente.render(self.string, False, color_yellow_2)
        self.image = self.text
        self.pos = (self.pos[0], self.pos[1] - self.speed)

        self.rect = self.image.get_rect(center = self.pos)
        screen.blit(self.image, self.rect)

class Chest( pygame.sprite.Sprite ):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Graphics\Clases\chest.png"), (64,64))
        self.closed_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.open = False
        self.open_image = pygame.transform.scale(pygame.image.load("Graphics\Clases\chest_open.png"), (64,64))
        self.count = 0
    def update(self):
        if self.count == 60:
            self.open = not self.open
            self.count = 0
        if self.open:
            self.image = self.open_image
        else:
            self.image = self.closed_image

        self.count += 1
