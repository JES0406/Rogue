import pygame
import random
from constantes import *
from clases import *

pygame.init()
termine = False
string = "Érase una vez una joven lechera que llevaba un cubo de leche en la cabeza, camino al mercado para venderla. Durante el camino, la soñadora joven iba imaginando lo que podría lograr conseguir con la leche. Pensó que en primer lugar y con el dinero de la venta compraría un canasto de huevos, los cuales una vez eclosionaran le permitiría montar una pequeña granja de pollos. Una vez estos crecieran podría venderlos, lo que le daría dinero para comprarse un lechón.Una vez este creciera la venta del animal bastaría para comprarse una ternera, con la leche de la cual seguiría obteniendo beneficios y a su vez podría tener terneros. Sin embargo, mientras iba pensando todas estas cosas la joven tropezó, lo que provocó que el cántaro cayera el suelo y se rompiera. Y con él, sus expectativas hacia lo que podría haber hecho con ella.”Este cuento, que cuenta con versiones de Esopo y La Fontaine (siendo este último el que hemos reflejado), nos enseña la necesidad de vivir en el presente y que a pesar de que soñar es necesario también debemos tener en cuenta que ello no basta para lograr nuestros propósitos. Inicialmente, es una pequeña historia que nos avisa de tener cuidado con que la ambición no nos haga perder el sentido.Asimismo, en algunas adaptaciones se incluye también un diálogo posterior entre la lechera y su madre, quien le cuenta que gracias a tener fantasías parecidas pudo lograr montar una granja: en este caso es una reflexión de que necesitamos soñar y ambicionar, pero cuidando lo que hacemos para llegar a cumplir los objetivos, además de no rendirnos ante el primer tropiezo u obstáculo."
tamaño_pantalla = 30
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
                termine = True
            else:
                while string[c] != " ":
                    c -= 1
                print(len(string))
                string_separated.append(string[:c])
                string = string[c:]
            c = 0
    c += 1

class Texto(pygame.sprite.Sprite):
    def __init__(self, string, pos, size, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.fuente = pygame.font.Font("Fuentes/starjedi/Starjedi.ttf", size)
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
    text_group.add(Texto(string_separated[i], (ANCHO//2, ALTO//2 + 70*i), 70))

while running and termine:
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