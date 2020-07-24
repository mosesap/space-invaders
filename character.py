from sprite import *
from lazer import lazer

class character(sprite):
    
    def __init__(self, filename, rows, cols, x_pos, y_pos, x_vel, y_vel):
        super().__init__(filename, rows, cols)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.magazine_group = pyg_sprite.Group()
        self.magazine_size = 10
        self.reload_clock = 0
        self.reload_time = 2
        
    def move(self, screen_width = 0, screen_height = 0):
        if screen_width == screen_width == 0:
            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
        else:
            #x-axis position
            self.x_pos += self.x_vel
            if self.x_pos > screen_width - self.cell_center[0]:
                self.x_pos = screen_width - self.cell_center[0]
            elif self.x_pos < self.cell_center[0]:
                self.x_pos = self.cell_center[0]
            #y-axis position
            self.y_pos += self.y_vel
            if self.y_pos > screen_height - self.cell_center[1]:
                self.y_pos = screen_height - self.cell_center[1]
            elif self.y_pos < self.cell_center[1]:
                self.y_pos = self.cell_center[1]
        self.rect = Rect(self.x_pos, self.y_pos, self.cell_height/2, self.cell_width/2)
    
    def shoot(self):
        if len(self.magazine_group) < self.magazine_size:
            self.magazine_group.add(lazer("sprites\lazer.png", 1, 6, self.x_pos, self.y_pos, 0, -10))
        elif self.reload_clock == 0:
            self.reload_clock = time.time()
        elif self.reload_clock != 0:
            if (time.time() - self.reload_clock) >= 2:
                self.magazine_group.empty() 
                self.reload_clock = 0