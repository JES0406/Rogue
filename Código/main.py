import pygame, sys, random, math, time, os
import funciones_globales as fn 
from constantes import *
from clases import Player


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
                    player = pygame.sprite.GroupSingle()
                    player.add(Player(clase))
                    nombre_state = False
                    juego_state = True
                if event.key == pygame.K_BACKSPACE:
                    nombre_str = nombre_str[:-1]
                elif event.key == pygame.K_SPACE:
                    nombre_str += "  "
                else:
                    if len(nombre_str) < LONGITUD_NOMBRE:
                        nombre_str += event.unicode.upper()

        elif juego_state:
            ### Start moving here
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    escena = 1
                    juego_state = False
                    end_state = True

        elif end_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if escena == 2:
                        end_state = False
                    else:
                        escena += 1
                    


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

        pygame.draw.rect(screen, color_black, (25, 300, ANCHO-40, 285), border_radius=20)
        pygame.draw.rect(screen, color_white, (35, 310, ANCHO-60, 265), border_radius=20)
        counter = 0
        while counter < 3:
            for i in range (0, 9):
                fn.text(f"{abecedario[i+counter*9]}", (50 + i*85, 360 + counter*85), 55)
            counter += 1


    elif juego_state:
        screen.fill(color_white)
        player.update()
        player.draw(screen)

    elif end_state:
        if escena == 1:
            screen.fill(color_green)
            fn.text_box(show)
            fn.admins(True, (400, 500), True, (400, 500))
            fn.text(f"Gracias por jugar a iMAT", (100, 530),20)
            fn.text(f"Esperamos que te haya gustado.", (100, 550), 20)
            fn.text(f"Presiona ENTER para ver tus estadisticas.", (100, 570), 20)

            hide()
        elif escena == 2:
            screen.fill(color_white)
            pygame.draw.rect(screen, color_black, (110, 90, 580, 200), border_radius=20)
            pygame.draw.rect(screen, color_white, (120, 100, 560, 180), border_radius=20)
            fn.text(f"Estadisticas:", (220, 150), 40)
            fn.text(f"Nombre: {nombre_str.rstrip()}", (220, 200), 40)
            fn.text(f"Clase: {clase}", (220, 250), 40)
        



    
    else:
        screen.fill((0,255,0))

    
    pygame.display.update()
    clock.tick(fps)