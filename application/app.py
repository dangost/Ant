import pygame
from collections import deque


class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
        self.x, self.y = pos
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def run(self):
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value

        size = self.app.cell_size
        rect = self.x * size, self.y * size, size - 1, size - 1
        if value:
            pygame.draw.rect(self.app.screen, pygame.Color('white'), rect)
        else:
            pygame.draw.rect(self.app.screen, self.color, rect)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.cols
        self.y = (self.y + dy) % self.app.rows


class App:
    def __init__(self, width=1600, height=900, cell_size=12):
        pygame.init()
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()

        self.cell_size = cell_size
        self.rows, self. cols = height // cell_size, width // cell_size
        self.grid = [[0 for col in range(self.cols)] for row in range(self.rows)]

        self.ant = Ant(app=self, pos=[self.cols // 2, self.rows // 2], color=pygame.Color("orange"))

    def run(self):
        while 1:
            self.ant.run()

            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.flip()
            self.clock.tick()


if __name__ == "__main__":
    app = App()
    app.run()

