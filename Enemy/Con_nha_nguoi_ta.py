import pygame
import os
from enemy import Enemy

width = 23
height = 40
imgs = []
for i in range(0,2):
    base_dirname = os.path.dirname(os.path.dirname(__file__))
    image_load = pygame.image.load(os.path.join(base_dirname, "asset/Enemy/", "Connhanguoita" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Con_nha_nguoi_ta(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.width = 23
        self.height = 40
        self.speed = self.init_speed * 3
        self.max_health = 5500
        self.current_health = self.max_health