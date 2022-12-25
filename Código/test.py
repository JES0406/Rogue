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