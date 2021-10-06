import pygame
import os
from enemies.enemy import Enemy

imgs = []
imgs.append(pygame.transform.scale(pygame.image.load("bocap1.png"),(64, 64)))
imgs.append(pygame.transform.scale(pygame.image.load("bocap2.png"),(64, 64)))

class Scorpion(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "scorpion"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]



