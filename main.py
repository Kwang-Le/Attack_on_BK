import pygame
from pygame.math import Vector2
import os
import random
from Enemy.SInh_vien import Sinh_vien
from tower import Tower
from archertower import ArcherTowerLong
win = pygame.display.set_mode((800, 450))


class Game:
    def __init__(self):
        self.width = 800
        self.height = 450
        self.waypoints = [(435, 138), (464, 148), (704, 153), (717, 164), (715, 349), (699, 358), (463, 360), (442, 380), (425, 404), (426, 446), (438, 12)]
        self.bg = pygame.image.load(os.path.join("asset", "16662.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.win = win
        self.enemys = []
        self.wave = 0
        self.last_spawn = 0

    def run(self):
        run = True
        interval = 0
        clock = pygame.time.Clock()
        archer = ArcherTowerLong()
        while run:
            clock.tick(60)
            now = pygame.time.get_ticks()
            if now - self.last_spawn > interval:
                self.last_spawn = now
                self.enemys.append(Sinh_vien(self.waypoints, win))
                interval = random.choice([1000, 2000, 3000, 4000, 5000])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                '''if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)'''
            self.draw()
            for i in self.enemys:
                i.move()
                i.draw_images()
            archer.attack(self.enemys)
            archer.draw(self.win)
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
