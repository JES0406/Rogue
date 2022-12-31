import pygame, random, math, time, os
from constantes import *
import funciones_globales as fn
from clases import Player, Enemy

user = Player("Caballero")
player = pygame.sprite.GroupSingle()
player.add(user)
enemies = pygame.sprite.Group()
enemy = Enemy((random.randint(0,ANCHO), random.randint(0,ALTO)), "Melee")
enemies.add(enemy)

show = True
contador = 0
contador2 = 0
while running:
    fn.update_camera_pos(user)
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(user.position)
    player.update()
    enemies.update(user)
    enemies.draw(screen)
    player.draw(screen)


    pygame.display.flip()
    clock.tick(fps)