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
            self.HP = 100
            self.hitpoint = 10
            self.regen = 1
            self.range = 10
            self.mana = 0
        elif class_chosen == "Mago": 
            self.speed = 2
            self.HP = 60
            self.hitpoint = 20
            self.regen = 1
            self.range = 60
            self.mana = 250
        elif class_chosen == "Arquero": 
            self.speed = 6
            self.HP = 40
            self.hitpoint = 20
            self.regen = 0.5
            self.range = 60
            self.mana = 0
        elif class_chosen == "Curandero": 
            self.speed = 4
            self.HP = 80
            self.hitpoint = 5
            self.regen = 2
            self.range = 60
            self.mana = 100
