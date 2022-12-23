import pygame, sys, random, math, time, os
import funciones_globales as gf 
import inicio as inic
import movimiento as mov
from constantes import *

estado = "inicio"
nombre = ""
dificultad = ""


running = True
while running:
    screen.fill(color_black)
    for evento in pygame.event.get(): #Para revisar todas las posibles interacciones
        if evento.type == pygame.QUIT:
            running = False
        if estado == "inicio":
            inic.int_string_evento(evento)
        if estado == "juego":
            inic.juego_evento(evento)

    if estado == "inicio":
        inic.inicio_bucle()
        if dificultad != "" and nombre != "":
            estado = "juego"

    elif estado == "juego":
        mov.juego_bucle()
        # enemy_list.append(enemy(enemy_id, color_list[enemy_id % 2]))
        # enemy_id += 1

    pygame.display.flip()
    clock.tick(60)

