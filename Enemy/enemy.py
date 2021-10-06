import pygame
import os

class Enemy:

    def __init__(self):
        self.width = 15
        self.height = 30
        self.imgs = []
        self.img = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),"asset/Enemy/","Sinhvien0.png")).convert_alpha(), (self.width, self.height))
        self.img_num = 0
        self.path = [(10, 224),(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 492), (740, 504), (580, 542), (148, 541), (10, 442), (-20, 335), (-75, 305), (-100, 345)] #path to go through the map, position of center
        self.x = self.path[0][0] # first x and y of enemy
        self.y = self.path[0][1]
        self.max_health = 1
        self.current_health = 1


    def draw_images(self, win):
        """Draw enemies' animations hihi.
        win: game surface."""
        self.img = self.imgs[self.img_num]
        draw_pos = (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2)
        win.blit(self.img, draw_pos)

    def draw_health_bar(self, win):
        """Draw enemies' health bar hihi.
        win: game surface."""




