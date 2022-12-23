import pygame

# Fuentes
def cargar_fuentes():
    dic_fuentes = {}
    fuente_titulo = pygame.font.Font("Fuentes/Japo/Japanese 3017.ttf", 50)
    fuente_general = pygame.font.Font("Fuentes/Pixel/Minecraft.ttf", 30)
    dic_fuentes["titulo"]  = fuente_titulo
    dic_fuentes["general"] = fuente_general
    return dic_fuentes

# Textos
def input_string(string, dic_menu, screen):
    string_surf = dic_menu["fuentes"]["general"].render(f"{string}", False, "white")
    string_rect = string_surf.get_rect(midleft = (500, 340))
    screen.blit(string_surf,string_rect)
    # Se usa para mostrar el string escrito por el user

def int_string_evento(evento, string, estado_local, lista_estados_locales):
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

    