import pygame, sys, random, math
from constantes import *
import funciones_globales as fn
import movimiento as mov

pygame.init()
pygame.display.set_caption("iMAT") #Título


# Funciones
def cargar_inicio():
    dic_menu = {}

    # Fuentes
    dic_fuentes = fn.cargar_fuentes()

    # Textos
    dic_textos = {}

    titulo = dic_fuentes["titulo"].render("Title placeholder", False, color_green)
    titulo_rect = titulo.get_rect(center = (400,170))
    tupla_titulo = (titulo, titulo_rect)

    int_nombre = dic_fuentes["general"].render("Introduce tu nombre: ", False, color_white)
    int_nombre_rect = int_nombre.get_rect(midright = (500,340))
    tupla_int_nombre = (int_nombre, int_nombre_rect)

    int_dificultad = dic_fuentes["general"].render("Inserte la dificultad: ", False, color_white)
    int_dificultad_rect = int_dificultad.get_rect(midright = (500,340))
    tupla_int_dificultad = (int_dificultad, int_dificultad_rect)

    dic_textos["titulo"] = tupla_titulo
    dic_textos["int_nombre"] = tupla_int_nombre
    dic_textos["int_dificultad"] = tupla_int_dificultad

    dic_menu["fuentes"] = dic_fuentes
    dic_menu["textos"] = dic_textos

    # Acceso a dic_menu: dic_menu["Clase que necesites"]["Objeto dentro de la clase"]

    return dic_menu

# Bucles
def inicio_bucle(dic_menu, estado_local):
    nombre, dificultad = "", ""
    if estado_local == "nombre":
        screen.blit(dic_menu["textos"]["titulo"][0], dic_menu["textos"]["titulo"][1])
        screen.blit(dic_menu["textos"]["int_nombre"][0], dic_menu["textos"]["int_nombre"][1])
        int_string(string)
        nombre = string
    if estado_local == "dificultad":
        screen.blit(dic_menu["textos"]["titulo"][0], dic_menu["textos"]["titulo"][1])
        screen.blit(dic_menu["textos"]["int_dificultad"][0], dic_menu["textos"]["int_dificultad"][1])
        int_string(string)   
        dificultad = string

    return nombre, dificultad

def juego_bucle():
    global enemy_list, color_list
    pwidth = 32
    pheight = 32
    playerpos = [20, 20]
    pspeed = 5
    mov_r = False
    mov_l = False
    mov_u = False
    mov_d = False
        
    moving_speed = mov.setspeed()
    ### Actual movement of the player
    if mov_l and playerpos[0] > 0: playerpos[0] -= moving_speed
    if mov_r and playerpos [0] < ANCHO - pwidth: playerpos[0] += moving_speed
    if mov_u and playerpos[1] > 0: playerpos[1] -= moving_speed
    if mov_d and playerpos[1] < ALTO - pheight: playerpos[1] += moving_speed


    pygame.draw.rect(screen, color_green, pygame.Rect(playerpos[0], playerpos[1], pwidth, pheight), width = 0)
    for bad_guy in enemy_list: 
        bad_guy.move(playerpos)
        pygame.draw.rect(screen, color_list[bad_guy.type], pygame.Rect(bad_guy.position[0], bad_guy.position[1], pwidth, pheight), width = 0)

# Bucles eventos
def int_string_evento(evento):
    global string, estado_local, lista_estados_locales
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN:
            print(f"{estado_local.capitalize()}: {string}")
            string = ""
            if estado_local != lista_estados_locales[len(lista_estados_locales) - 1]:
                estado_local = lista_estados_locales[lista_estados_locales.index(estado_local) + 1]
            else:
                estado_local = lista_estados_locales[0]
        elif evento.key == pygame.K_BACKSPACE:
            string = string[:-1]
        else:
            string += evento.unicode

def juego_evento(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT: mov_l = True
        if evento.key == pygame.K_RIGHT: mov_r = True
        if evento.key == pygame.K_UP: mov_u = True
        if evento.key == pygame.K_DOWN: mov_d = True
        if evento.key == pygame.K_SPACE:
            mov.addenemy(random.randint(0,1))
            print(len(enemy_list))
        if evento.key == pygame.K_TAB:
            for i in range(300):
                mov.addenemy(random.randint(0,1))
                print(len(enemy_list))

        ### Stop moving here
    elif evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT:
            mov_l = False
        if evento.key == pygame.K_RIGHT:
            mov_r = False
        if evento.key == pygame.K_UP:
            mov_u = False
        if evento.key == pygame.K_DOWN:
            mov_d = False

    
    # Devuelve un string de las teclas pulsadas

def int_string(string):
    global dic_menu
    string_surf = dic_menu["fuentes"]["general"].render(f"{string}", False, "white")
    string_rect = string_surf.get_rect(midleft = (500, 340))
    screen.blit(string_surf,string_rect)

    # Se usa para mostrar el string escrito por el user

# Eventos

estado = "inicio"

estado_local = "nombre"


dic_menu = cargar_inicio()

string = ""

enemy_list = []
enemy_id = 0
color_list = [color_red, color_white]

running = True
while running:
    screen.fill(color_black)
    for evento in pygame.event.get(): #Para revisar todas las posibles interacciones
        if evento.type == pygame.QUIT:
            running = False
        if estado == "inicio":
            int_string_evento(evento)
        if estado == "juego":
            juego_evento(evento)

    if estado == "inicio":
        inicio_bucle(dic_menu, estado_local)
        if dificultad != "" and nombre != "":
            estado = "juego"

    elif estado == "juego":
        juego_bucle()
        # enemy_list.append(enemy(enemy_id, color_list[enemy_id % 2]))
        # enemy_id += 1
        

    
    pygame.display.flip()
    clock.tick(60)