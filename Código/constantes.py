import pygame
# Colores
color_black = '#333333'
color_green = '#48e5c2'
color_white = '#fcfaf9'
color_red = '#ce5e5e'
color_blue = '#5e9ece'
color_yellow = '#f2e05e'
color_gray_1 = '#f2f2f2'
color_gray_2 = '#e6e6e6'
color_red_2 = '#8B0000'
color_yellow_2 = '#FFD700'
color_green_2 = '#006400'
color_blue_2 = '#00008B'
# Propiedades
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fps = 60
LONGITUD_NOMBRE = 10

mapwidth = 2 * ANCHO
mapheight = 2 * ALTO
camera_left_top = [0,0]

running = True
inicio_state = True
class_state = False
nombre_state = False
juego_state = False
level_up = False
pausa_state = False
shoot = False
ability = False
clase = ""
enemy_list = []

choice = ""
enemy_timer = 0

abecedario = [chr(i + 65) for i in range(26)]; abecedario.append(' ') # Lo mismo pero este le gusta a David porque está DRY 😉 JAajjajaja

enemy_types = ["Melee", "Ranged"]
