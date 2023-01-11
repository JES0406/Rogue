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
color_black_1 = (0,0,0)
# Propiedades
ANCHO = 800
ALTO = 600
ticks_per_frame = 10
frames_per_animation_loop = 6
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fps = 60
LONGITUD_NOMBRE = 10
tamaño_pantalla = 30
speed_1 = 1
speed_2 = 10
speed_3 = -10


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
end_state = False
shoot = False
ability = False
slash = False
sped_up = False
show = True
death_state = False
extra_counter = 0
clase = ""
enemy_list = []
enemy_bullets = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()
enemeies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
text_group = pygame.sprite.Group()
bushes = pygame.sprite.Group()

choice = ""
enemy_timer = 0
enemy_spawn_rate = 60
p = 0
dead_counter = 0

abecedario = [chr(i + 65) for i in range(26)]; abecedario.append(' ') # Lo mismo pero este le gusta a David porque está DRY 😉 JAajjajaja

enemy_types = ["Melee", "Ranged"]

adjetivos = ['valiente', 'hermoso', 'torpe', 'odiado', 'temido', 'avaricioso', 'astuto', 'incauto']
hazanhas = [
'el concepto de L(S)', 'el teorema de Reflexividad Dual', 'la equivalencia del logaritmo', 'las V.A. multivariantes',
'su fallo en el examen de física', 'la diapositiva de "el hecho religioso"', 'el motivo de modularizar el código',
'las sumas de series telescópicas', 'cómo funcionan los objetos de Python', 'los diccionarios de Python',
'la fórmula de Bernoulli para fluidos',
'por qué sus compañeros del MTC eran tan inútiles', 'la clase del día anterior de David Alfaya',
'la temperatura a la que hay que poner el aire acondicionado en clase para que la gente no se queje',
'la manera de escanear el QR de asistencia a la primera', 'de dónde había conseguido rascar 0,25 puntos en cálculo',
'los ejercicios de topología en 3 o más dimensiones',
'la demostración de la desigualdad triangular aplicada a la distancia euclídea',
'la clave para seguir las explicaciones de MATLAB de David Alfaya sin quedarse atrás',
'qué es una condición necesaria pero no suficiente', 'la manera de sobornar a David Alfaya para que te apruebe',
'las preguntas 10 del MTC de Álgebra y Cálculo', 'por qué no le funciona el matplotlib.pyplot',
'el diseño óptimo de péndulo para sacar mediciones legibles en phyphox y además no estampar su móvil en el proceso',
'que estudiar la semana de antes no ayuda casi nada y hay que llevar el temario al día',
'los anuladores de subespacios vectoriales', 'los problemas de la hoja B sin mirar las soluciones',
'la manera de identificar una serie numérica y el criterio a utilizar en cada caso',
'para qué sirven los créditos de las asignaturas',
]
c_for_time = 0