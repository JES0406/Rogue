import pygame
# Colores
color_black = '#333333'
color_green = '#48e5c2'
color_white = '#fcfaf9'
color_red = '#ce5e5e'
color_blue = '#5e9ece'
color_gray_1 = '#f2f2f2'
color_gray_2 = '#e6e6e6'
# Propiedades
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fps = 60
LONGITUD_NOMBRE = 10

# Listas importantes
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
enemy_types = ["Melee", "Ranged"]

