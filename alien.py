from sprite import *
from lazer import lazer
import random

class alien(sprite):
    
    def __init__(self, filename, rows, cols, x_pos, y_pos, x_vel = 0, y_vel = 0):
        super().__init__(filename, rows, cols)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.magazine_group = pyg_sprite.Group()

    def move(self, screen_width, screen_height):
        self.x_pos += self.x_vel
        if self.x_pos > screen_width - self.cell_center[0]:
            self.x_pos = screen_width - self.cell_center[0]
            self.x_vel *= -1
        elif self.x_pos < self.cell_center[0]:
            self.x_pos = self.cell_center[0]
            self.x_vel *= -1
        self.y_pos += self.y_vel
        if self.y_pos > screen_height/2 - self.cell_center[1]:
            self.y_pos = screen_height/2 - self.cell_center[1]
            self.y_vel *= -1
        elif self.y_pos < self.cell_center[1]:
            self.y_pos = self.cell_center[1]
            self.y_vel *= -1
        self.rect = Rect(self.x_pos, self.y_pos, self.cell_height/2, self.cell_width/2)

    def shoot(self):
        if 1 == random.randint(1,20):
            self.magazine_group.add(lazer("sprites\lazer.png", 1, 6, self.x_pos, self.y_pos, 0, 10))