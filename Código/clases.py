import math
import pygame
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