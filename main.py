import pygame
from pygame.math import Vector2
import os
# from Enemy import Enemy
from SInh_vien import Sinh_vien
from tower import Tower
win = pygame.display.set_mode((800, 450))


class Game:
    def __init__(self):
        self.width = 800
        self.height = 450
        self.waypoints = [(619, 208), (621, 451), (-15, 210)]
        self.bg = pygame.image.load(os.path.join("asset", "BK_map.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.enemies = []
        self.win = win

    def run(self):
        run = True
        clock = pygame.time.Clock()
        # enemy = Enemy(self.waypoints[len(self.waypoints) - 1], self.waypoints, win)
        enemy = Sinh_vien(self.waypoints[len(self.waypoints) - 1], self.waypoints, win)
        tower = Tower()

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
            for point in self.waypoints:
                pygame.draw.rect(win, (90, 200, 40), (point, (4, 4)))
            enemy.move()
            enemy.draw()
            tower.draw(self.win)
            tower.draw_radius(self.win)
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
