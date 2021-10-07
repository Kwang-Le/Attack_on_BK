import pygame
import os
from .enemy import Enemy

width = 18
height = 40
imgs = []
for i in range(0,2):
    base_dirname = os.path.dirname(os.path.dirname(__file__))
    image_load = pygame.image.load(os.path.join(base_dirname, "asset/Enemy/", "Sinhvien" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Sinh_vien(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.max_health = 1000
        self.current_health = self.max_health
        self.speed = self.init_speed * 1
        self.width = 18
        self.height = 40
