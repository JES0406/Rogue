import pygame
import colores as col


pygame.init()
ANCHO = 800
ALTO = 400
screen = pygame.display.set_mode((ANCHO, ALTO)) #Crear una pantalla
pygame.display.set_caption("Título") #Título
clock = pygame.time.Clock()




# Funciones
def cargar_inicio():
    dic_menu = {}

    # Fuentes
    dic_fuentes = {}

    fuente_titulo = pygame.font.Font("Fuentes/Japo/Japanese 3017.ttf", 50)
    fuente_general = pygame.font.Font("Fuentes/Pixel/Minecraft.ttf", 30)
    dic_fuentes["titulo"]  = fuente_titulo
    dic_fuentes["general"] = fuente_general

    # Textos
    dic_textos = {}

    titulo = fuente_titulo.render("Title placeholder", False, col.color_green)
    titulo_rect = titulo.get_rect(center = (400,170))
    tupla_titulo = (titulo, titulo_rect)

    int_nombre = fuente_general.render("Introduce tu nombre: ", False, col.color_white)
    int_nombre_rect = int_nombre.get_rect(midright = (500,340))
    tupla_int_nombre = (int_nombre, int_nombre_rect)

    int_dificultad = fuente_general.render("Inserte la dificultad: ", False, col.color_white)
    int_dificultad_rect = int_dificultad.get_rect(midright = (500,340))
    tupla_int_dificultad = (int_dificultad, int_dificultad_rect)

    dic_textos["titulo"] = tupla_titulo
    dic_textos["int_nombre"] = tupla_int_nombre
    dic_textos["int_dificultad"] = tupla_int_dificultad

    dic_menu["fuentes"] = dic_fuentes
    dic_menu["textos"] = dic_textos

    # Acceso a dic_menu: dic_menu["Clase que necesites"]["Objeto dentro de la clase"]

    return dic_menu

def inicio_bucle(dic_menu, estado_local):
    if estado_local == "nombre":
        screen.fill(col.color_black)
        screen.blit(dic_menu["textos"]["titulo"][0], dic_menu["textos"]["titulo"][1])
        screen.blit(dic_menu["textos"]["int_nombre"][0], dic_menu["textos"]["int_nombre"][1])
        int_string(string)
    if estado_local == "dificultad":
        screen.fill(col.color_black)
        screen.blit(dic_menu["textos"]["titulo"][0], dic_menu["textos"]["titulo"][1])
        screen.blit(dic_menu["textos"]["int_dificultad"][0], dic_menu["textos"]["int_dificultad"][1])
        int_string(string)   

def int_string_evento(evento):
    global string, estado_local, lista_estados_locales
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN:
            print(string)
            string = ""
            if estado_local != lista_estados_locales[len(lista_estados_locales) - 1]:
                estado_local = lista_estados_locales[lista_estados_locales.index(estado_local) + 1]
            else:
                estado_local = lista_estados_locales[0]
        elif evento.key == pygame.K_BACKSPACE:
            string = string[:-1]
        else:
            string += evento.unicode
    
    # Devuelve un string de las teclas pulsadas

def int_string(string):
    global dic_menu
    string_surf = dic_menu["fuentes"]["general"].render(f"{string}", False, "white")
    string_rect = string_surf.get_rect(midleft = (500, 340))
    screen.blit(string_surf,string_rect)

    # Se usa para mostrar el string escrito por el user

# Eventos
lista_estados = ["inicio"]
estado = "inicio"

lista_estados_locales = ["nombre", "dificultad"]
estado_local = "nombre"


dic_menu = cargar_inicio()

string = ""


running = True
while running:
    for evento in pygame.event.get(): #Para revisar todas las posibles interacciones
        if evento.type == pygame.QUIT:
            running = False
        if estado == "inicio":
            int_string_evento(evento)
    if estado == "inicio":
        inicio_bucle(dic_menu, estado_local)


    pygame.display.update()
    clock.tick(60)