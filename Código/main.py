import pygame, sys, random, math, time, os
import funciones_globales as fn 
from constantes import *
from clases import Player, Button, Enemy, Projectile, Texto


pygame.init()
pygame.display.set_caption("iMAT") #Título


def hide():
    global show, contador
    if contador != fps:
        if contador == fps//2:
            show = not show
        contador += 1
    else:
        contador = 0
        show = not show
def draw_minimap(user):
    pygame.draw.rect(screen, 'White', pygame.Rect(0,0,ANCHO / 4 + 2, ALTO / 4 +2))
    pygame.draw.rect(screen, 'Black', pygame.Rect(0,0,ANCHO / 4, ALTO / 4))
    pygame.draw.rect(screen, color_green, pygame.Rect(user.position[0]/8,user.position[1]/8,user.size[0]/8, user.size[0]/8))

def divide_str(string):
    string_separated = []
    c = 0
    termine = False
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
    if termine:
        return string_separated

class Bush(pygame.sprite.Sprite):
    def __init__(self,choice = "1"):
        super().__init__(bushes)
        if choice == "1":
            self.image = pygame.transform.scale(pygame.image.load("Graphics/Fondos/Decoration/bush_1.png").convert_alpha(), (100, 60))
        elif choice == "2":
            self.image = pygame.transform.scale(pygame.image.load("Graphics/Fondos/Decoration/bush_2.png").convert_alpha(), (100, 150))
        elif choice == "3":
            self.image = pygame.transform.scale(pygame.image.load("Graphics/Fondos/Decoration/bush_3.png").convert_alpha(), (100, 80))
        self.pos = (random.randint(0, mapwidth), random.randint(0, mapheight))
        self.rect = self.image.get_rect(center = self.pos)

    def update(self):
        self.rect = self.image.get_rect(center = (fn.relative_pos(self.pos, 0), fn.relative_pos(self.pos, 1)))
while len(bushes) < 100:
    bush = Bush(random.choice(["1", "2", "3"]))
    if not pygame.sprite.spritecollideany(bush, bushes):  
        bushes.add(bush)
    print(len(bushes))
    
        
    


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
                        escena += 1
                if event.key == pygame.K_ESCAPE:
                    inicio_state = True
                    class_state = False

        elif nombre_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_str == "":
                        nombre_str = "EMPTY_NAME"
                    user = Player(clase)
                    player.add(user)
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
            if level_up:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        level_up_state = False
                    choice += event.unicode.upper()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausa_state = True 
                    
                    if event.key == pygame.K_SPACE:
                        ability = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and ability:
                        target = (fn.relative_pos(pygame.mouse.get_pos(), 0) + camera_left_top[0], fn.relative_pos(pygame.mouse.get_pos(), 1) + camera_left_top[1])
                        user.ability(target)
                if pygame.mouse.get_pressed()[2]:
                    shoot = True
                if user.class_chosen != "Caballero":
                    if shoot and not pygame.mouse.get_pressed()[2]:
                        target = (pygame.mouse.get_pos()[0] + camera_left_top[0], pygame.mouse.get_pos()[1] + camera_left_top[1])
                        bullets.add(Projectile(user.position, target, user.proyectile_size, user.proyectile_speed, user.hitpoint, user.proyectile, 1000))
                        shoot = False
                else:
                    if shoot and not pygame.mouse.get_pressed()[2] and not slash:
                        slash = True
                        target = (pygame.mouse.get_pos()[0] + camera_left_top[0], pygame.mouse.get_pos()[1] + camera_left_top[1])
                        angle = math.degrees(math.atan2(user.position[1] - target[1], user.position[0] - target[0]))
                        pos = (user.relative_pos[0] - 50 * math.cos(math.radians(angle)), user.relative_pos[1] - 50 * math.sin(math.radians(angle)))

                        slash_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Graphics/Clases/proyectiles/slash.png")\
                            .convert_alpha(), (75, 75)), angle)
                        slash_rect = slash_img.get_rect(center = pos)
                        slash_count = 0
                        shoot = False
                

        elif end_state:
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
            class_image = fn.chosen_sprite(clase, 1)
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
        class_image = fn.chosen_sprite(clase, 1)
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
        fn.update_camera_pos(user)
        fn.background("game")
        if user.exp >= user.exp_to_level:
            level_up_state= True
            user.exp -= user.exp_to_level
            user.level += 1
            user.exp_to_level = 100 * user.level + user.exp_to_level
        if level_up_state:
            fn.background("level_up")
            HP_button = Button((50, 400), (120, 80), "HP", color_green, color_green_2, color_black)
            Mana_button = Button((225, 400), (120, 80), "Mana", color_blue, color_blue_2, color_black)
            speed_button = Button((425, 400), (120, 80), "Speed", color_yellow, color_yellow_2, color_black)
            damage_button = Button((600, 400), (120, 80), "Damage", color_red, color_red_2, color_black)
            
            button_list = [HP_button, Mana_button, speed_button, damage_button]
            for button in button_list:
                button.update()
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0]:
                        choice = button.name
                        user.level_up(choice)
                        level_up_state = False
                        choice = ""
            count = 0
            if count == 20:
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
        elif death_state:
            for i in enemeies:
                i.kill()
            fondo = pygame.transform.scale(pygame.image.load(f"Graphics/Fondos/dead.png").convert_alpha(), (ANCHO, ALTO))
            fondo_rect = fondo.get_rect(center = (ANCHO/2, ALTO/2))
            screen.blit(fondo, fondo_rect)
            if fondo_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                juego_state = False
                end_state = True
                escena = 1
        else:
            enemy_timer += 1
            if enemy_timer == int(enemy_spawn_rate):
                enemy_pos = (random.randint(0, ALTO- 50), random.randint(0, ANCHO - 100))
                enemeies.add(Enemy(enemy_pos, random.choice(enemy_types)))
                p += 1
                enemy_timer = 0
            if p == 10:
                enemy_spawn_rate *= 0.9
                p = 0
                
            enemies_hit = pygame.sprite.groupcollide(enemeies, bullets, False, True)
            for enemy in enemies_hit:
                enemy.HP -= user.hitpoint
            
            for enemy in enemies_hit:
                enemy.HP -= user.hitpoint
            sprite_hit = pygame.sprite.spritecollide(user, enemy_bullets, True)
            for bullet in sprite_hit:
                user.HP -= bullet.damage

            
            bushes.update()
            bushes.draw(screen)
            player.update()
            if user.frame >= 6:
                death_state = True
                print(c_for_time)
                minutos = c_for_time//3600
                segundos = c_for_time//60 - minutos*60
            
            
            enemeies.update(user)
            bullets.update()
            enemy_bullets.update()
            player.draw(screen)
            enemeies.draw(screen)
            if slash:
                screen.blit(slash_img, slash_rect)
                for i in enemeies:
                    if slash_rect.colliderect(i.rect):
                        i.HP -= user.hitpoint
                for i in enemy_bullets:
                    if slash_rect.colliderect(i.rect):
                        i.copy = Projectile(i.position, (fn.relative_pos((math.sin(i.angle - 90) * 100, math.cos(i.angle-90) * 100), 0), fn.relative_pos((math.sin(i.angle -90) *100, math.cos(i.angle-90)*100), 1))\
                            , i.size, i.speed, i.damage, i.weapon, i.time_to_destroy)
                        i.kill()
                        bullets.add(i.copy)
                        print("Parry this you filthy casual")
                        bullets.update()
                        enemy_bullets.update()
                slash_count += 1
                if slash_count == 10:
                    slash = False
                    slash_count = 0
            
            bullets.draw(screen)
            enemy_bullets.draw(screen)
            
            draw_minimap(user)
            c_for_time += 1

    elif end_state:
        if escena == 1:
            screen.fill(color_black_1)
            if len(text_group) == 0:
                creditos = divide_str(f"Aquí yace {nombre_str.rstrip()}, el {clase} más {random.choice(adjetivos)} que haya visto este reino. Tardó {minutos} minutos con {segundos} segundos en morir. La leyenda dice que entendió \"{random.choice(hazanhas)}\" justo antes de morir.")
                for i in range(len(creditos)):
                    text_group.add(Texto(creditos[i], (ANCHO//2, ALTO + 70*i), 70, 1))
            text_group.update()
            text_group.draw(screen)
            print(text_group.sprites()[-1].size)
            if text_group.sprites()[-1].size == 0:
                text_group.empty()
                escena = 2
        if escena == 2:
            screen.fill(color_black_1)
            if len(text_group) == 0:
                creditos = divide_str(f"Gracias por jugar a iMAT.Nos ha costado mucho trabajo hacer este proyecto; esperamos que te haya gustado y hasta la versión 1.0.")
                for i in range(len(creditos)):
                    text_group.add(Texto(creditos[i], (ANCHO//2, ALTO + 70*i), 70, 1))
            text_group.update()
            text_group.draw(screen)
            if text_group.sprites()[-1].size == 0:
                text_group.empty()
                escena = 3
        if escena == 3:
                fuente = pygame.font.Font("Fuentes/starjedi/Starjhol.ttf", 70)
                text = fuente.render("@", True, color_yellow_2)
                rect = text.get_rect(center = (ANCHO//2, ALTO//2))
                screen.blit(text, rect)




    else:
        screen.fill((0,255,0))

    extra_counter += 0.0001
    pygame.display.update()
    clock.tick(fps)