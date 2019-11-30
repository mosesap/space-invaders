import pygame
import time

class sprite:

    def __init__(self, filename, rows, cols):
        self.sheet = pygame.image.load(filename)
        self.rows = rows
        self.cols = cols
        self.cell_count = rows * cols
        self.rect = self.sheet.get_rect()
        w = self.cell_width = self.rect.width / cols
        h = self.cell_height = self.rect.height / rows
        hw, hh = self.cell_center = (w/2, h/2)
        self.cells = list([(index % cols * w, 0, w, h) for index in range(self.cell_count)])
        self.handle = list([(0,0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h),])

    def draw(self, surface, cellindex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellindex])

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
        #should try deleting object once it leaves the map's bounds

class alien(sprite):
    
    def __init__(self, filename, rows, cols, x_pos, y_pos, x_vel = 0, y_vel = 0):
        super().__init__(filename, rows, cols)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self, screen_width, screen_height):
        self.x_pos += self.x_vel
        if self.x_pos > screen_width - self.cell_center[0]:
            self.x_pos = screen_width - self.cell_center[0]
            self.x_vel *= -1
        elif self.x_pos < self.cell_center[0]:
            self.x_pos = self.cell_center[0]
            self.x_vel *= -1
        self.y_pos += self.y_vel
        if self.y_pos > screen_height - self.cell_center[1]:
            self.y_pos = screen_height - self.cell_center[1]
            self.y_vel *= -1
        elif self.y_pos < self.cell_center[1]:
            self.y_pos = self.cell_center[1]
            self.y_vel *= -1
    
        

class character(sprite):
    
    def __init__(self, filename, rows, cols, x_pos, y_pos, x_vel, y_vel):
        super().__init__(filename, rows, cols)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.magazine = []
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
    
    def shoot(self):
        if len(self.magazine) < self.magazine_size:
            self.magazine.append(lazer("sprites\lazer.png", 1, 6, self.x_pos, self.y_pos, 0, -10))
        elif self.reload_clock == 0:
            self.reload_clock = time.time()
        elif self.reload_clock != 0:
            if (time.time() - self.reload_clock) >= 2:
                self.magazine.clear #clear doesnt change the len() of the list
                self.magazine = [] # I think only this line works
                self.reload_clock = 0
            



