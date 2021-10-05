import pygame
from pygame.math import Vector2
import os
from Enemy import Enemy
win = pygame.display.set_mode((800, 450))


class Game:
    def __init__(self):
        self.width = 800
        self.height = 450
        self.waypoints = [(435, 138), (464, 148), (704, 153), (717, 164), (715, 349), (699, 358), (463, 360), (442, 380), (425, 404), (426, 446), (438, 12)]
        self.bg = pygame.image.load(os.path.join("asset", "16662.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []

    def run(self):
        run = True
        clock = pygame.time.Clock()
        enemy = Enemy(self.waypoints[len(self.waypoints) - 1], self.waypoints, win)
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
            self.draw()
            enemy.move()
            enemy.draw()
            for point in self.waypoints:
                pygame.draw.rect(win, (90, 200, 40), (point, (4, 4)))
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        win.blit(self.bg, (0, 0))
        # win.fill((255, 255, 255))
        pygame.display.set_caption("Attack_on_BK")
        for click in self.clicks:
            pygame.draw.circle(win, (255,0,0), (click[0],click[1]), 5,0)
        # pygame.display.update()

G = Game()
G.run()
