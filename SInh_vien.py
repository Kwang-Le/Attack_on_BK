import pygame
import os
from Enemy import Enemy

width = 20
height = 40
imgs = []
for i in range(0, 2):
    image_load = pygame.image.load(os.path.join("asset/Enemy/", "Sinhvien" + str(i) + ".png"))
    image_load = pygame.transform.flip(image_load, True, False)
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Sinh_vien(Enemy):

    def __init__(self, pos, waypoints, win):
        super().__init__(pos, waypoints, win)
        self.imgs = imgs[:]