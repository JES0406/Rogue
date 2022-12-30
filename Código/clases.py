import math, random, pygame, sys, time, os
from constantes import *
import funciones_globales as fn
# class Enemy:
    # def __init__(self, speed, range, position:tuple, type):
    #     global pwitdh, pheight, enemy_id, color_list, screen
    #     self.type = type
    #     self.speed = speed
    #     self.range = range + pwidth
    #     self.position = [position[0], position[1]]
    #     global enemy_id
    #     self.id = enemy_id
    #     enemy_id += 1
    # def move(self, target:list):
    #         ### Ranged enemy movement
    #     distance_x = target[0] - self.position[0]
    #     distance_y = target[1] - self.position[1]
    #     distance = math.sqrt(distance_x**2 + distance_y **2)
    #     if distance < self.range: 
    #         ranged_espeed_vector = -self.speed
    #     elif abs(distance - self.range) < self.speed: ranged_espeed_vector = 0 
    #     else: ranged_espeed_vector = self.speed
    #     if self.position[0] < self.speed + target[0]: self.position[0] += ranged_espeed_vector
    #     elif self.position[0] > self.speed + target[0]: self.position[0] -= ranged_espeed_vector
    #     if self.position[1] < self.speed + target[1]: self.position[1] += ranged_espeed_vector
    #     elif self.position[1] > self.speed + target[1]: self.position[1] -= ranged_espeed_vector

class Player(pygame.sprite.Sprite):
    def __init__(self, class_chosen):
        pygame.sprite.Sprite.__init__(self)
        self.image = fn.chosen_sprite(class_chosen)
        self.position = [ANCHO//2, ALTO//2]
        self.rect = self.image.get_rect(center = (ANCHO//2, ALTO//2))
        if class_chosen == "Caballero": 
            self.speed = 4
            self.MaxHP = 100
            self.hitpoint = 10
            self.HPregen = 0.1
            self.range = 10
            self.MaxMana = 0
        elif class_chosen == "Mago": 
            self.speed = 2
            self.MaxHP = 60
            self.hitpoint = 20
            self.HPregen = 0.1
            self.range = 60
            self.MaxMana = 250
        elif class_chosen == "Arquero": 
            self.speed = 6
            self.MaxHP = 40
            self.hitpoint = 20
            self.HPregen = 0.05
            self.range = 60
            self.MaxMana = 0
        elif class_chosen == "Curandero": 
            self.speed = 4
            self.MaxHP = 80
            self.hitpoint = 5
            self.HPregen = 0.2
            self.range = 60
            self.MaxMana = 100

        self.Manaregen = 0.2
        self.exp = 0
        self.level = 0
        self.HP = self.MaxHP
        self.Mana = self.MaxMana
        self.exp_to_level = 100 * self.level
        
    def health_bar(self):
        pygame.draw.rect(screen, color_red, (self.rect.x, self.rect.y - 10, self.rect.width, 5))
        pygame.draw.rect(screen, color_green, (self.rect.x, self.rect.y - 10, self.rect.width * (self.HP/self.MaxHP), 5))

    def mana_bar(self):
        try:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))
            pygame.draw.rect(screen, color_blue, (self.rect.x, self.rect.y - 5, self.rect.width * (self.Mana/self.MaxMana), 5))
        except ZeroDivisionError:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))

    def level_up(self, choice):
            if choice == "HP":
                self.MaxHP += 10
                self.HPregen += 0.01
            elif choice == "Mana":
                self.MaxMana += 10
                self.Manaregen += 0.01
            elif choice == "Speed":
                self.speed += 0.2
            elif choice == "Damage":
                self.hitpoint += 1
            

    def exp_bar(self):
        try:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 15, self.rect.width, 5))
            pygame.draw.rect(screen, color_white, (self.rect.x, self.rect.y - 15, self.rect.width * (self.exp/self.exp_to_level), 5))
        except ZeroDivisionError:
            pygame.draw.rect(screen, color_white, (self.rect.x, self.rect.y - 15, self.rect.width, 5))
        

    def update(self):
        self.health_bar()
        self.mana_bar()
        if self.HP < self.MaxHP:
            self.HP += self.HPregen
        if self.Mana < self.MaxMana:
            self.Mana += self.Manaregen
        self.exp_bar()
    
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
        if type == "Melee":
            self.HP = 100
            self.range = 10
            self.image = pygame.transform.scale(pygame.image.load("Graphics/Clases/knight.png").convert_alpha(), (80, 80))
            self.speed = 1
        elif type == "Ranged":
            self.HP = 50
            self.range = 100
            self.image = pygame.transform.scale(pygame.image.load("Graphics/Clases/archer.png").convert_alpha(), (80, 80))
            self.speed = 2
        self.position = [pos[0], pos[1]]
        self.rect = self.image.get_rect(center = (self.position[0], self.position[1]))
        self.size = self.image.get_size()
        self.range += self.size[0]
        
        

    
    def move(self, player):
        # move towards player but stay in range
        distance_x = player.position[0] - self.position[0]
        distance_y = player.position[1] - self.position[1]
        distance = math.sqrt(distance_x**2 + distance_y **2)
        if distance < self.range: 
            ranged_espeed_vector = -self.speed
        elif abs(distance - self.range) < self.speed: ranged_espeed_vector = 0 
        else: ranged_espeed_vector = self.speed
        if self.position[0] < self.speed + player.position[0]: self.position[0] += ranged_espeed_vector
        elif self.position[0] > self.speed + player.position[0]: self.position[0] -= ranged_espeed_vector
        if self.position[1] < self.speed + player.position[1]: self.position[1] += ranged_espeed_vector
        elif self.position[1] > self.speed + player.position[1]: self.position[1] -= ranged_espeed_vector


    def update(self, player):
        self.move(player)
        self.rect = self.image.get_rect(center = (self.position[0], self.position[1]))
        if self.HP <= 0:
            self.kill()
            player.exp += 10
        self.HP -= 1
            




    
        
        
