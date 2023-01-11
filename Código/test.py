import pygame, random, math, time, os
from constantes import *
import funciones_globales as fn
from clases import Player, Enemy
# class Chest( pygame.sprite.Sprite ):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load("Graphics\Clases\chest.png"), (64,64))
#         self.closed_image = self.image
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.open = False
#         self.open_image = pygame.transform.scale(pygame.image.load("Graphics\Clases\chest_open.png"), (64,64))
#         self.count = 0
#     def update(self):
#         if self.count == 60:
#             self.open = not self.open
#             self.count = 0
#         if self.open:
#             self.image = self.open_image
#         else:
#             self.image = self.closed_image

#         self.count += 1
# chests = pygame.sprite.Group()

sheet = pygame.image.load(f"Pixel Crawler-FREE-1.8\Heroes\Knight\Death\Death-Sheet.png").convert_alpha()
sheet_size = sheet.get_size()
knight_size = sheet_size[0]/6

sheet_1 = pygame.image.load(f"Pixel Crawler-FREE-1.8\Heroes\Wizzard\Death\Death-Sheet.png").convert_alpha()
sheet_1_size = sheet.get_size()
mage_size = sheet_1_size[0]/6
def get_image(sheet, width, height, color, frame):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0,0), (0 + width*frame, 0, width + width*frame, height))
    image = pygame.transform.scale(image, (width*2, height*2))
    image.set_colorkey(color)
    return image

def frame_list_maker(sheet, frame_size, color_black_1, frames_number):
    frame_list = []
    for frame in range(0,frames_number):
        frame_list.append(get_image(sheet, frame_size, frame_size, color_black_1, frame))
    return frame_list 

knight_list = frame_list_maker(sheet, knight_size, color_black_1, 6)

mage_list = frame_list_maker(sheet_1, 48, color_black_1, 6)

contador = 0
frame = 0
while running:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(knight_list[frame], (0, 0))
    screen.blit(mage_list[frame], (0, mage_size))

    if contador % 10 == 0:
        if frame == 5:
            frame = 0
        else:
            frame += 1
    contador += 1
    pygame.display.flip()
    clock.tick(fps)