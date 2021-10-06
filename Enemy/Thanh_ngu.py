import pygame
import os
from enemy import Enemy

width = 15
height = 30
imgs = []
for i in range(0,2):
    base_dirname = os.path.dirname(os.path.dirname(__file__))
    image_load = pygame.image.load(os.path.join(base_dirname, "asset/Enemy/", "thanhngu" + str(i) + ".png"))#.convert_alpha()
    imgs.append(pygame.transform.scale(image_load, (width, height)))

class Thanh_ngu(Enemy):

    def __init__(self):
        self.imgs = imgs[:]