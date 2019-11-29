import pygame
from sprite import sprite

#init pygame
pygame.init()
W = 400
H = 300
HW = W/2
HH = H/2
#create screen
screen = pygame.display.set_mode((W, H))
screen.fill((0, 0, 0))
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load("icon.png")
#pygame.display.set_icon(icon)

#spaceship
spaceship = sprite("sprites\spaceship.png", 1, 6)
CENTER_HANDLE = 4
ship_index = 0

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    spaceship.draw(screen, ship_index % spaceship.cell_count, HW, HH, CENTER_HANDLE)
    ship_index += 1

    pygame.display.update()
    screen.fill((0, 0, 0))