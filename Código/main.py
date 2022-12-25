import pygame, sys, random, math, time, os
import funciones_globales as fn 
from constantes import *


pygame.init()
pygame.display.set_caption("iMAT") #Título

running = True
inicio_state = True
class_state = False
nombre_state = False
juego_state = False
clase = "Caballero"

def hide():
    global show, contador
    if contador != fps:
        if contador == fps//2:
            show = not show
        contador += 1
    else:
        contador = 0
        show = not show

show = True

contador = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if inicio_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nombre_str = "" * 10
                    inicio_state = False
                    class_state = True
                    escena = 1

        elif class_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if escena == 2:
                        class_state = False
                        nombre_state = True
                        n = random.randint(1, 4)
                        if n == 1:
                            clase = "Caballero"
                        elif n == 2:
                            clase = "Mago"
                        elif n == 3:
                            clase = "Arquero"
                        elif n == 4:
                            clase = "Curandero"
                        c = 0
                    else:
                        escena += 1

        elif nombre_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_str == "":
                        nombre_str = "EMPTY_NAME"
                    nombre_state = False
                    juego_state = True
                if event.key == pygame.K_BACKSPACE:
                    nombre_str = nombre_str[:-1]
                elif event.key == pygame.K_SPACE:
                    nombre_str += "  "
                else:
                    if len(nombre_str) < LONGITUD_NOMBRE:
                        nombre_str += event.unicode.upper()
                


    if inicio_state:
        fn.background("inicio")
        fn.text_box(show)
        fn.admins(True, (400, 500), True, (400, 500))
        fn.text(f"Hola, somos Marcos y Javi, los creadores de este juego.", (100, 530),20)
        fn.text(f"Esperamos que te guste.", (100, 550), 20)
        fn.text(f"Presiona ENTER para continuar.", (100, 570), 20)
        
        hide()
        
        
    elif class_state:
        if escena == 1:
            fn.background("class")
            fn.text_box(show)
            fn.admins(True,(600, 500), False, (0, 500))
            fn.text(f"Tras pulsar en la clase que quieras podrás empezar", (100, 530),20)
            fn.classes()

            hide()

        elif escena == 2:
            fn.background("class")
            fn.text_box(show)
            fn.admins(False, (0, 500), True, (600, 500))
            fn.text(f"OsTrAs...", (100, 550), 60)
            fn.text(f"Casi se nos olvida.", (350, 560), 20)

            hide()

    elif nombre_state:
        fn.background("nombre", clase)
        pygame.draw.rect(screen, color_black, (110, 90, 580, 200), border_radius=20)
        pygame.draw.rect(screen, color_white, (120, 100, 560, 180), border_radius=20)
        try:
            for i in range (0, LONGITUD_NOMBRE):
                pygame.draw.rect(screen, color_black, (257 + i*35, 230, 25, 4), border_radius=20)
                fn.text(f"{nombre_str[i]}", (255 + i*35, 215), 45)
        except IndexError:
            for j in range (0, LONGITUD_NOMBRE - len(nombre_str)):
                pygame.draw.rect(screen, color_black, (257 + (i+j)*35, 230, 25, 4), border_radius=20)
        class_image = fn.chosen_sprite(clase)
        class_rect = class_image.get_rect(center = (170, 150))
        screen.blit(class_image, class_rect)
        fn.text(f"Como te llamas?", (220, 150), 40)
        



    
    else:
        screen.fill((0,255,0))

    
    pygame.display.update()
    clock.tick(fps)