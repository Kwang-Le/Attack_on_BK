import pygame
import os
from enemy import Enemy

width = 21
height = 60
imgs = []
for i in range(0,2):
    base_dirname = os.path.dirname(os.path.dirname(__file__))
    image_load = pygame.image.load(os.path.join(base_dirname, "asset/Enemy/", "NguoiconcuaDang" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Nguoi_con_cua_Dang(Enemy):

    def __init__(self, waypoints, win):
        super().__init__(waypoints, win)
        self.imgs = imgs[:]
        self.width = 21
        self.height = 60
        self.max_health = 3500
        self.current_health = self.max_health
        self.speed = self.init_speed * 3
