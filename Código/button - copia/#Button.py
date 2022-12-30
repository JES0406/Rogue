#Button

import pygame 

pygame.font.init()
screen = pygame.display.set_mode((800,600))

bg_color = '#3972a9'
running = True




fonts = ["Código/button - copia/fuente.ttf"]



class Button():
    def __init__(self, left_top:tuple, width_height:tuple, text = 'Menu', color1 = '#823999', color2 = '#182300', text_color = 'White', font = 0):
        placeholder = ' ' + text + ' '
        self.font = pygame.font.Font(fonts[font], int((width_height[0]*1.5)//len(placeholder)))
        self.text_surface = self.font.render(placeholder, False, text_color) #text, anti aliasing, color
        self.pos = left_top
        self.size = width_height
        self.color = (color1,color2)
        self.rect = pygame.Rect(left_top[0],left_top[1],width_height[0],width_height[1])

    def update(self):
        self.hovering = False
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > self.pos[0] and mousepos[0] < self.pos[0] + self.size[0]:
            if mousepos[1] > self.pos[1] and mousepos[1] < self.pos[1] + self.size[1]: self.hovering = True
        pygame.draw.rect(screen,self.color[self.hovering],self.rect, border_radius=10)
        screen.blit(self.text_surface, (self.pos[0],self.pos[1] + 20))


button1 = Button((100,300),(200,100), text_color = 'Black', text = 'pito')

while running:

    screen.fill(bg_color)
    button1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()