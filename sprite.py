import pygame

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
