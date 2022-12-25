import pygame, sys, random, math
from constantes import *
import funciones_globales as fn
import Código.movimiento as mov

def bucle_fin():
    global puntuacion
    screen.fill(color_black)
    fin_text = fn.cargar_fuentes()["titulo"].render("Fin del juego", False, color_white)
    fin_text_rect = fin_text.get_rect(center = (400, 200))
    screen.blit(fin_text, fin_text_rect)

    puntuacion_text = fn.cargar_fuentes()["general"].render("Puntuación: " + str(puntuacion), False, color_white)
    puntuacion_text_rect = puntuacion_text.get_rect(center = (400, 300))
    screen.blit(puntuacion_text, puntuacion_text_rect)

    