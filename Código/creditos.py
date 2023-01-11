import pygame
import random
from constantes import *
from clases import *

pygame.init()
termine = False
string = "En un punto de la historia indeterminado, dos amigos fueron a Austria a esquiar, ¿Qué destino les deparará?, ¿perderán el tren?, ¿Se romperan las piernas?; sólo el destino lo sabe"
c = 0
string_separated = []
speed_1 = 1
speed_2 = 10
speed_3 = -10
while c < len(string):
    if len(string) < tamaño_pantalla:
        string_separated.append(string)
        c = tamaño_pantalla
    else:    
        if c == tamaño_pantalla:
            if string[c] == " " or string[c] == "," or string[c] == "." or string[c] == ";":
                string_separated.append(string[:tamaño_pantalla])
                string = string[tamaño_pantalla:]
                termine = True
            else:
                if string.count(" ")>= 1:
                    while string[c] != " " and string[c] != "," and string[c] != "." and string[c] != ";":
                        c -= 1
                print(len(string))
                string_separated.append(string[:c])
                string = string[c:]
            c = 0
    c += 1
if len(string) <= tamaño_pantalla:
    termine = True
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
    
    def change_speed(self, speed):
        self.speed = speed

    def update(self):
        if self.size >= 0:
            self.size = (self.pos[1])/6
            if self.size < 0:
                self.size = 0
        print(self.size)
        self.fuente = pygame.font.Font("Fuentes/starjedi/Starjedi.ttf", int(self.size))
        self.text = self.fuente.render(self.string, False, color_yellow_2)
        self.image = self.text
        self.pos = (self.pos[0], self.pos[1] - self.speed)

        self.rect = self.image.get_rect(center = self.pos)
        screen.blit(self.image, self.rect)
text_group = pygame.sprite.Group()
for i in range(len(string_separated)):
    text_group.add(Texto(string_separated[i], (ANCHO//2, ALTO + 70*i), 70, 1))

while running and termine:
    screen.fill(color_black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                if event.key == pygame.K_RETURN and not sped_up:
                    for text in text_group:
                        text.change_speed(speed_3)
                        sped_up = True
            if event.key == pygame.K_RETURN and not sped_up:
                for text in text_group:
                    text.change_speed(speed_2)
                    sped_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                for text in text_group:
                    text.change_speed(speed_1)
                    sped_up = False
    text_group.update()
    text_group.draw(screen)
    pygame.display.update()
    clock.tick(fps)