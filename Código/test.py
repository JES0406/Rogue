import pygame

pygame.init()
pygame.display.set_caption("iMAT") #Título

ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fps = 60

# Imagenes
marcos = pygame.image.load("Graphics/Creadores/recortado_marcos.png")
marcos_rect = marcos.get_rect(bottomleft = (400,500))

javi = pygame.image.load("Graphics/Creadores/recortado_javi.png")
javi_rect = javi.get_rect(bottomright = (400,500))



def background():
    screen.blit(pygame.image.load("Graphics/Fondos/fondo.png"), (0,0))

def text_box():
    pygame.draw.rect(screen, (255,255,255), (0,500,800,100))

def text(texto, posicion):
    fuente = pygame.font.Font(None, 30)
    texto = fuente.render(texto, True, (0,0,0))
    screen.blit(texto, posicion)

def hiding():
    global show
    global contador
    global contador2
    if show:
        contador += 1
        if contador == 300:
            show = False
            contador = 0
    else:
        contador2 += 1
        if contador2 == 300:
            show = True
            contador2 = 0

    if show:
        screen.blit(pygame.image.load("Graphics/Fondos/fondo.png"), (0,0))
        screen.blit(marcos, marcos_rect)
        screen.blit(javi, javi_rect)
        text_box()
        text(f"Hola, somos Marcos y Javi, los creadores de este juego.", (400, 530))
        text(f"Esperamos que te guste.", (400, 570))
    else:
        screen.blit(pygame.image.load("Graphics/Fondos/fondo.png"), (0,0))
        screen.blit(marcos, marcos_rect)
        screen.blit(javi, javi_rect)
        text_box()



show = True
contador = 0
contador2 = 0
while True:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    background()
    screen.blit(marcos, marcos_rect)
    screen.blit(javi, javi_rect)
    text_box()
    text(f"Hola, somos Marcos y Javi, los creadores de este juego.", (400, 530))
    text(f"Esperamos que te guste.", (400, 570))

    hiding()



    pygame.display.flip()
    clock.tick(fps)