import pygame, random, math, time, os
from constantes import *
import funciones_globales as fn
from clases import Player, Enemy
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
chests = pygame.sprite.Group()


fila = 0
contador = 0
contador_2 = 0
while running:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if 20 + 70 * contador_2 > ANCHO - 140:
        print("boom")
        fila += 70
        contador_2 = 0

    if contador == 60:
        chests.add(Chest(100 + fila,20 + 70 * contador_2))
        contador = 0
        contador_2 += 1

    chests.update()
    chests.draw(screen)
    contador += 1

    pygame.display.flip()
    clock.tick(fps)