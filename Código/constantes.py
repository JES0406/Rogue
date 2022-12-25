import pygame
# Colores
color_black = '#333333'
color_green = '#48e5c2'
color_white = '#fcfaf9'
color_red = '#ce5e5e'
# Propiedades
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fps = 60
LONGITUD_NOMBRE = 10

# Listas importantes
lista_estados = ["inicio", "juego"]
lista_estados_locales = ["nombre", "dificultad"]