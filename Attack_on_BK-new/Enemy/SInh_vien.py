import pygame
import os
from .enemy import Enemy

width = 18
height = 40
imgs = []
for i in range(0,2):
    image_load = pygame.image.load(os.path.join("asset/Enemy/", "Sinhvien" + str(i) + ".png"))
    # image_load = pygame.transform.flip(image_load, True, False)
    imgs.append(pygame.transform.scale(image_load, (width, height)))
class Sinh_vien(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.max_health = 1000
        self.current_health = self.max_health
        self.speed = self.init_speed * 3
        self.money = 1
        self.width = 18
        self.height = 40
        self.min_speed = self.speed / 2
        self.normal_speed = self.init_speed * 3
        self.max_speed = self.speed

    def slow(self):
        self.speed = self.max_speed / 2

    def un_slow(self):
        self.speed = self.max_speed
