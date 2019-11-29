import pygame

#init pygame
pygame.init()
#create screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load("icon.png")
#pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 56, 170))
    pygame.display.update()