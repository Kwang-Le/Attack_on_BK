import pygame
import os
from .enemy import Enemy

width = 40
height = 26

imgs = []
for i in range(0,2):
    image_load = pygame.image.load(os.path.join("asset/Enemy/", "thanhngu" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Thanh_ngu(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.max_health = 800
        self.current_health = self.max_health
        self.speed = self.init_speed * 1
        self.money = 1
        self.width = width
        self.height = height
        self.min_speed = self.speed / 2
        self.normal_speed = self.init_speed * 1
        self.max_speed = self.speed
        self.hoc_bong = 100

    def slow(self):
        self.speed = self.max_speed / 2

    def un_slow(self):
        self.speed = self.max_speed