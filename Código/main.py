import pygame, sys, random, math, time, os
import funciones_globales as fn 
from constantes import *
from clases import Player, Button, Enemy


pygame.init()
pygame.display.set_caption("iMAT") #Título

running = True
inicio_state = True
class_state = False
nombre_state = False
juego_state = False
level_up = False
pausa_state = False
clase = ""
enemy_list = []

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

bushes = pygame.sprite.Group()

for i in range(10):
    bush_pos = (random.randint(0, ANCHO), random.randint(0, ALTO))
    bush = pygame.sprite.Sprite(bushes)
    bush.image = pygame.transform.scale(pygame.image.load("Graphics/Fondos/Decoration/bush_1.png"), (100, 80))
    bush.rect = bush.image.get_rect(center = bush_pos)
    


contador = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
                    else:
                        if clase == "":
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
                        escena += 1
                if event.key == pygame.K_ESCAPE:
                    inicio_state = True
                    class_state = False

        elif nombre_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_str == "":
                        nombre_str = "EMPTY_NAME"
                    player = pygame.sprite.GroupSingle()
                    user = Player(clase)
                    player.add(user)
                    choice = ""
                    enemy_timer = 0
                    enemeies = pygame.sprite.Group()
                    nombre_state = False
                    juego_state = True
                elif event.key == pygame.K_BACKSPACE:
                    nombre_str = nombre_str[:-1]
                elif event.key == pygame.K_SPACE:
                    nombre_str += "  "
                elif event.key == pygame.K_ESCAPE:
                    class_state = True
                    nombre_state = False
                else:
                    if len(nombre_str) < LONGITUD_NOMBRE:
                        nombre_str += event.unicode.upper()

        elif juego_state:
            ### Start moving here
            if level_up_state:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        level_up_state = False
                    choice += event.unicode.upper()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        escena = 1
                        juego_state = False
                        end_state = True
                    if event.key == pygame.K_ESCAPE:
                        pausa_state = True
                    if event.key == pygame.K_UP:
                        user.rotate("up")
                    if event.key == pygame.K_DOWN:
                        user.rotate("down")
                    if event.key == pygame.K_LEFT:
                        user.rotate("left")
                    if event.key == pygame.K_RIGHT:
                        user.rotate("right")
                

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
            fn.text(f"Tras pulsar en la clase que quieras podrás empezar", (100, 530),20)
            button_list = fn.classes()
            fn.admins(True,(600, 500), False, (0, 500)) 
            for button in button_list:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0]:
                        # print(button.name)
                        clase = button.name
                        escena = 2           

            hide()

        elif escena == 2:
            fn.background("class")
            fn.text_box(show)
            fn.admins(False, (0, 500), True, (600, 500))
            fn.text(f"OsTrAs...", (100, 550), 60)
            fn.text(f"Casi se nos olvida.", (350, 560), 20)
            fn.text(f"Clase: {clase}", (150, 150), 20)
            class_image = fn.chosen_sprite(clase)
            class_rect = class_image.get_rect(center = (210, 210))
            screen.blit(class_image, class_rect)
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
        letter_buttons = []
        while counter < 3:
            for i in range (0, 9):
                letter_button = Button((35 + i*82, 310 + counter*82), (70,70), abecedario[i+ 9*counter], color_white, color_gray_1)
                letter_buttons.append(letter_button)
                letter_buttons[i+ 9*counter].update()
                fn.text(f"{abecedario[i + 9*counter]}", (50 + i*82, 350 + counter*82), 55)
            counter += 1
        for button in letter_buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if len(nombre_str) < LONGITUD_NOMBRE:
                        nombre_str += button.name
    elif juego_state:
        print(user.exp, user.exp_to_level, user.level, user.HP)
        fn.background("game")
        bushes.draw(screen)
        if user.exp >= user.exp_to_level:
            level_up_state= True
            user.level += 1
            user.exp_to_level = 100 * user.level + user.exp_to_level
        if level_up_state:
            fn.background("level_up")
            user.level_up(choice)
            count = 0
            if count == 60:
                level_up_state = False
                count = 0
            else:
                count += 1
        elif pausa_state:
            pygame.draw.rect(screen, color_black, (140, 90, 580, ALTO - 150), border_radius=20)
            pygame.draw.rect(screen, color_white, (150, 100, 560, ALTO - 170), border_radius=20)
            fn.text(f"PAUSA", (350, 150), 60)
            continue_button = Button((160, 200), (500, 100), "Continuar", color_white, color_gray_2, color_black)   
            continue_button.update()
            if continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    pausa_state = False
            exit_button = Button((160, 350), (500, 100), "Guardar y Salir", color_white, color_gray_2, color_black)
            exit_button.update()
            if exit_button.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    running = False
            
        else:
            enemy_timer += 1
            if enemy_timer == 60:
                enemy_pos = (random.randint(0, ALTO- 50), random.randint(0, ANCHO - 100))
                enemeies.add(Enemy(enemy_pos, random.choice(enemy_types)))
                enemy_timer = 0
                
            player.update()
            enemeies.update(user)
            player.draw(screen)
            enemeies.draw(screen)

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