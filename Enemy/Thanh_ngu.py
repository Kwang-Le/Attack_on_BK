import pygame
import os
from enemy import Enemy

height = 30
width = 41
imgs = []
for i in range(0,2):
    base_dirname = os.path.dirname(os.path.dirname(__file__))
    image_load = pygame.image.load(os.path.join(base_dirname, "asset/Enemy/", "thanhngu" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Thanh_ngu(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs[:]
        self.max_health = 2000
        self.current_health = self.max_health
        self.width = 41
        self.height = 30
        self.speed = 0.03
