import pygame
import os
from .enemy import Enemy

width = 19
height = 40
imgs = []
for i in range(0, 2):
    image_load = pygame.image.load(os.path.join("asset/Enemy/", "SanBK" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class San_BK(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.max_health = 4000
        self.current_health = self.max_health
        self.speed = self.init_speed * 2
        self.money = 2
        self.width = 19
        self.height = 40
        self.min_speed = self.speed / 2
        self.normal_speed = self.init_speed * 2
        self.max_speed = self.speed

    def slow(self):
        self.speed = self.max_speed / 2

    def un_slow(self):
        self.speed = self.max_speed