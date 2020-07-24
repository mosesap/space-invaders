from sprite import *

class lazer(sprite):

    def __init__(self, filename, rows, cols, x_pos, y_pos, x_vel = 0, y_vel = -20):
        super().__init__(filename, rows, cols)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
    
    def move(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.rect = Rect(self.x_pos, self.y_pos, self.cell_height/2, self.cell_width/2)