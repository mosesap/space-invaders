import pygame
from sprite import character

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
clock = pygame.time.Clock()

#icon = pygame.image.load("icon.png")
#pygame.display.set_icon(icon)

#spaceship
spaceship = character("sprites\spaceship.png", 1, 6, HW, HH, 0, 0)
CENTER_HANDLE = 4
index = 0

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship.x_vel = -5
            elif event.key == pygame.K_RIGHT:
                spaceship.x_vel = 5
            elif event.key == pygame.K_DOWN:
                spaceship.y_vel = 5
            elif event.key == pygame.K_UP:
                spaceship.y_vel = -5
            elif event.key == pygame.K_SPACE:
                spaceship.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                spaceship.x_vel = 0
            elif event.key == pygame.K_RIGHT:
                spaceship.x_vel = 0
            elif event.key == pygame.K_DOWN:
                spaceship.y_vel = 0
            elif event.key == pygame.K_UP:
                spaceship.y_vel = 0

    spaceship.move(W,H)
    spaceship.draw(screen, index % spaceship.cell_count, spaceship.x_pos, spaceship.y_pos, CENTER_HANDLE)
    index += 1
    for lazer in spaceship.magazine:
        lazer.move()
        lazer.draw(screen, index % lazer.cell_count, lazer.x_pos, lazer.y_pos, CENTER_HANDLE)

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)