from pygame import image
from pygame import sprite as pyg_sprite
from pygame import Rect
import time

class sprite(pyg_sprite.Sprite):

    def __init__(self, filename, rows, cols):
        pyg_sprite.Sprite.__init__(self)
        self.sheet = image.load(filename)
        self.rows = rows
        self.cols = cols
        self.cell_count = rows * cols
        self.sp_rect = self.sheet.get_rect()
        w = self.cell_width = self.sp_rect.width / cols
        h = self.cell_height = self.sp_rect.height / rows
        hw, hh = self.cell_center = (w/2, h/2)
        self.cells = list([(index % cols * w, 0, w, h) for index in range(self.cell_count)])
        self.handle = list([(0,0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h),])

    def draw(self, surface, cellindex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellindex])