import pygame
from pygame import display
from pygame import time
from pygame import image
from sprite import character
from sprite import alien

#init pygame
pygame.init()
width = 400
height = 300
half_width = width/2
half_height = height/2
#create screen
screen = display.set_mode((width, height))
screen.fill((0, 0, 0))
display.set_caption("Space Invaders")
clock = time.Clock()
display.set_icon(pygame.image.load("sprites\invader.png"))

#spaceship
spaceship = character("sprites\spaceship.png", 1, 6, half_width, half_height, 0, 0)
CENTER_HANDLE = 4
index = 0

#aliens
alien_list = []
num_aliens = 1
while len(alien_list) < num_aliens:
    alien_list.append(alien("sprites\invader.png", 1, 1, half_width/2, half_height/2, 6, 0))

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

    #MOVE AND DRAW
    spaceship.move(width,height)
    spaceship.draw(screen, index % spaceship.cell_count, spaceship.x_pos, spaceship.y_pos, CENTER_HANDLE)

    for lazer in spaceship.magazine:
        lazer.move()
        lazer.draw(screen, index % lazer.cell_count, lazer.x_pos, lazer.y_pos, CENTER_HANDLE)
        lazer.check_collision(alien_list[0])

    for alien in alien_list:
        alien.move(width, height)
        alien.draw(screen, index % alien.cell_count, alien.x_pos, alien.y_pos, CENTER_HANDLE)        

    index += 1
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)