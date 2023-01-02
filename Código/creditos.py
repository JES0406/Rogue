import pygame
import random
from constantes import *
from clases import *

pygame.init()

fuente = pygame.font.Font("Fuentes/starjedi/Starjhol.ttf", 50)
string = "It was a cold grey day in late November. The weather had changed overnight, when a backing wind brought a granite sky and a mizzling rain with it, and although it was now only a little after two o clock in the afternoon the pallor of a winter evening seemed to have closed upon the hills, cloaking them in mist.                                                                      Gracias por jugar a este juego. Espero que os haya gustado. Si queréis seguir conmigo, podéis seguirme en mi cuenta de Instagram: @marcos elcovids"
tamaño_pantalla = 20
c = 0
string_separated = []
speed_1 = 1
speed_2 = 10
while c < len(string):
    if len(string) < tamaño_pantalla:
        string_separated.append(string)
        c = tamaño_pantalla
    else:    
        if c == tamaño_pantalla:
            if string[c] == " ":
                string_separated.append(string[:tamaño_pantalla])
                string = string[tamaño_pantalla:]
            else:
                while string[c] != " ":
                    c -= 1
                string_separated.append(string[:c])
                string = string[c:]
            c = 0
    c += 1

class Texto(pygame.sprite.Sprite):
    def __init__(self, string, pos, size, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.fuente = pygame.font.Font("Fuentes/starjedi/Starjhol.ttf", size)
        self.text = self.fuente.render(string, False, color_yellow_2)
        self.rect = self.text.get_rect(center = pos)
        self.image = self.text
        self.pos = pos
        self.speed = speed
    
    def change_speed(self, speed):
        self.speed = speed

    def update(self):
        self.pos = (self.pos[0], self.pos[1] - self.speed)
        self.rect.center = self.pos
        screen.blit(self.text, self.rect)
text_group = pygame.sprite.Group()
for i in range(len(string_separated)):
    text_group.add(Texto(string_separated[i], (ANCHO//2, ALTO//2 + 50*i), 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not sped_up:
                for text in text_group:
                    text.change_speed(speed_2)
                    sped_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                for text in text_group:
                    text.change_speed(speed_1)
                    sped_up = False
    screen.fill(color_black)
    text_group.draw(screen)
    text_group.update()
    pygame.display.flip()
    clock.tick(fps)