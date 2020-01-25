import pygame
from pygame import display, time, image
from pygame import sprite as pyg_sprite
from sprite import character
from sprite import alien
#------------------------------------------------------------------------------
#init pygame
pygame.init()
width = 400
height = 300
half_width = width/2
half_height = height/2
#------------------------------------------------------------------------------
#create screen
screen = display.set_mode((width, height))
screen.fill((0, 0, 0))
display.set_caption("Space Invaders")
clock = time.Clock()
display.set_icon(pygame.image.load("sprites\invader.png"))
index = 0
#------------------------------------------------------------------------------
#spaceship
spaceship = character("sprites\spaceship.png", 1, 6, half_width, half_height, 0, 0)
CENTER_HANDLE = 4
#aliens
#TODO Properly position aliens
alien_group = pyg_sprite.Group()
num_aliens = 2
while len(alien_group) < num_aliens:
    alien_group.add(alien("sprites\invader.png", 1, 1, half_width/2, half_height/(num_aliens-len(alien_group) + 1), 6, 0))
#------------------------------------------------------------------------------
#GAME LOOP
#------------------------------------------------------------------------------
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
    for lazer in spaceship.magazine_group:
        lazer.move()
        lazer.draw(screen, index % lazer.cell_count, lazer.x_pos, lazer.y_pos, CENTER_HANDLE)
    for alien in alien_group:
        alien.move(width, height)
        alien.draw(screen, index % alien.cell_count, alien.x_pos, alien.y_pos, CENTER_HANDLE)        
    pyg_sprite.groupcollide(spaceship.magazine_group, alien_group, True, True, collided=None)
    #TICK
    index += 1
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)