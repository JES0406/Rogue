import pygame
import random
from constantes import *
from clases import *

# Textos

def text_box(show):
    pygame.draw.rect(screen, (255,255,255), (0, 500, 800, 100), 0, border_radius = 10)
    pygame.draw.rect(screen, (0,0,0), (8, 505, 785, 90), 2, border_radius = 10)
    pygame.draw.rect(screen, (0,0,0), (0, 500, 800, 100), 2, border_radius = 10)
    if show:
        pygame.draw.polygon(screen, (0,0,0), ((750,570), (770,570), (760,580)))
    else:
        pygame.draw.polygon(screen, (200,200,200), ((750,570), (770,570), (760,580)))

def text(string, pos, size):
    font = pygame.font.Font("Fuentes/Pixel/Minecraft.ttf", size)
    text = font.render(string, False, (0,0,0))
    text_rect = text.get_rect(midleft = pos)
    screen.blit(text, text_rect)

# Fondos
def background(state_str, role = None):
    if state_str == "inicio":
        string = "Fondo.jpg"
        imat = pygame.transform.scale(pygame.image.load("Graphics/Fondos/Logo.png").convert_alpha(), (ANCHO, ALTO-100))
        screen.blit(imat, (20,0))
    
    elif state_str == "class":
        string = "clase.png"

    elif state_str == "nombre":
        if role == "Caballero":
            string = "fondo_caballero.png"
        elif role == "Arquero":
            string = "fondo_arquero.png"
        elif role == "Mago":
            string = "fondo_mago.png"
        elif role == "Curandero":
            string = "fondo_curandero.png"
        else:
            string = "nombre.png"
        

    elif state_str == "game":
        string = "desierto.jpg"
    elif state_str == "level_up":
        string = "level_up.jpg"
        

    fondo = pygame.transform.scale(pygame.image.load(f"Graphics/Fondos/{string}").convert_alpha(), (ANCHO, ALTO))
    screen.blit(fondo, (0,0))
# Imagenes

def admins(marcos, pos_marcos, javi, pos_javi):
    if marcos:
        marcos = pygame.image.load("Graphics/Creadores/recortado_marcos.png")
        marcos_rect = marcos.get_rect(bottomleft = pos_marcos)
        screen.blit(marcos, marcos_rect)

    if javi:
        javi = pygame.image.load("Graphics/Creadores/recortado_javi.png")
        javi_rect = javi.get_rect(bottomright = pos_javi)
        screen.blit(javi, javi_rect)

def classes():
    knight_buttom = Button((120, 120), (570, 100), "Caballero", color_white, color_gray_1, color_white)
    knight_buttom.update()
    knight = pygame.transform.scale(pygame.image.load("Graphics/Clases/knight.png").convert_alpha(), (80, 80))
    knight_rect = knight.get_rect(midright = (195, 160))
    screen.blit(knight, knight_rect)
    text(f"Caballero: Personaje melee", (195, 160), 20)
    text(f"Mucha vida y dano medio.", (300, 180), 20)

    archer_buttom = Button((120, 220), (570, 100), "Arquero", color_white, color_gray_1, color_white)
    archer_buttom.update()
    archer = pygame.transform.scale(pygame.image.load("Graphics/Clases/archer.png").convert_alpha(), (80, 80))
    archer_rect = archer.get_rect(midright = (195, 260))
    screen.blit(archer, archer_rect)
    text(f"Arquero: Personaje a distancia", (195, 260), 20)
    text(f"Vida baja y dano muy alto.", (300, 280), 20)

    mage_buttom = Button((120, 320), (570, 100), "Mago", color_white, color_gray_1, color_white)
    mage_buttom.update()
    mage = pygame.transform.scale(pygame.image.load("Graphics/Clases/mage.png").convert_alpha(), (80, 80))
    mage_rect = mage.get_rect(midright = (195, 360))
    screen.blit(mage, mage_rect)
    text(f"Mago: Personaje a distancia", (195, 360), 20)
    text(f"Vida media y dano alto.", (300, 380), 20)

    healer_buttom = Button((120, 420), (570, 80), "Curandero", color_white, color_gray_1, color_white)
    healer_buttom.update()
    healer = pygame.transform.scale(pygame.image.load("Graphics/Clases/healer.png").convert_alpha(), (80, 80))
    healer_rect = healer.get_rect(midright = (195, 460))
    screen.blit(healer, healer_rect)
    text(f"Curandero: Personaje de apoyo", (195, 460), 20)
    text(f"Vida media y dano bajo.", (300, 480), 20)

    button_list = [knight_buttom, archer_buttom, mage_buttom, healer_buttom]
    return button_list

def chosen_sprite(choice):
    if choice == "Caballero":
        class_image = pygame.transform.scale(pygame.image.load("Graphics/Clases/knight.png").convert_alpha(), (100, 100))
    
    elif choice == "Arquero":
        class_image = pygame.transform.scale(pygame.image.load("Graphics/Clases/archer.png").convert_alpha(), (100, 100))
    
    elif choice == "Mago":
        class_image = pygame.transform.scale(pygame.image.load("Graphics/Clases/mage.png").convert_alpha(), (100, 100))

    elif choice == "Curandero":
        class_image = pygame.transform.scale(pygame.image.load("Graphics/Clases/healer.png").convert_alpha(), (100, 100))

    return class_image



