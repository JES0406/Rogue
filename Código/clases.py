import math, random, pygame, sys, time, os
from constantes import *
import funciones_globales as fn
class Enemy:
    def __init__(self, speed, range, position:tuple, type):
        global pwitdh, pheight, enemy_id, color_list, screen
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

class Player(pygame.sprite.Sprite):
    def __init__(self, class_chosen):
        pygame.sprite.Sprite.__init__(self)
        self.image = fn.chosen_sprite(class_chosen)
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
        # self.HP = self.MaxHP
        # self.Mana = self.MaxMana
        self.HP = 20
        self.Mana = 0
        
    def health_bar(self):
        pygame.draw.rect(screen, color_red, (self.rect.x, self.rect.y - 10, self.rect.width, 5))
        pygame.draw.rect(screen, color_green, (self.rect.x, self.rect.y - 10, self.rect.width * (self.HP/self.MaxHP), 5))

    def mana_bar(self):
        try:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))
            pygame.draw.rect(screen, color_blue, (self.rect.x, self.rect.y - 5, self.rect.width * (self.Mana/self.MaxMana), 5))
        except ZeroDivisionError:
            pygame.draw.rect(screen, color_black, (self.rect.x, self.rect.y - 5, self.rect.width, 5))

    
    def update(self):
        self.health_bar()
        self.mana_bar()
        if self.HP < self.MaxHP:
            self.HP += self.HPregen
        if self.Mana < self.MaxMana:
            self.Mana += self.Manaregen
        
