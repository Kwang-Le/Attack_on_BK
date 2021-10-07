import pygame
import math
import os

class Enemy:

    def __init__(self):
        self.width = 15
        self.height = 30
        self.imgs = []
        self.img = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),"asset/Enemy/","Sinhvien0.png")).convert_alpha(), (self.width, self.height))
        self.img_num = 0
        self.path = [(10, 224),(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83)] #path to go through the map, position of center
        self.path_pos = 0
        self.endpoint = (810, 83)
        self.x = self.path[0][0] # first x and y of enemy
        self.y = self.path[0][1]
        self.max_health = 1
        self.current_health = 1
        self.speed = 0

    def draw_images(self, win):
        """Draw enemies' animations hihi.
        win: game surface."""
        self.img = self.imgs[self.img_num]
        draw_pos = (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2)
        win.blit(self.img, draw_pos)
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """Draw enemies' health bar hihi.
        win: game surface."""
        green = (0,255,0)
        red = (255,0,0)
        draw_pos = (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 4)
        max_health = pygame.draw.rect(win, red, pygame.Rect(draw_pos,(self.width + 1, 2)))
        current_health = pygame.draw.rect(win, green, pygame.Rect(draw_pos,((self.width + 1)*(self.current_health/self.max_health), 2)))

    def is_hit(self, X, Y):
        """Check if bullets hit the enemy.
        X, Y: bullet's x,y.
        return boolean."""
        if (X >= self.x and X <= self.x + self.width) and (Y >= self.y and Y <= self.y + self.height):
            return True
        return False

    def damage(self, dmg):
        """Substracts enemy health.
        dmg: damage to substract.
        return current_health."""
        self.current_health -= dmg
        return self.current_health

    def dead(self):
        """Returns if enemy is dead or not"""
        if self.current_health <= 0:
            return True
        return False

    def move(self):
        """Moves enemy."""
        """self.img_num += 1
        if self.img_num >= len(self.imgs):
            self.img_num = 0"""

        if self.path_pos < len(self.path):
            x1, y1 = self.path[self.path_pos]
            if self.path_pos == len(self.path) - 1:
                x2, y2 = self.endpoint
            else:
                x2, y2 = self.path[self.path_pos + 1]

            length = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
            direction = ((x2 - x1)/length * self.speed, (y2 - y1)/length * self.speed)
            self.x, self.y = (self.x + direction[0], self.y + direction[1])

            if direction[0] >= 0: #move right
                if direction[1] >= 0: #move down
                    if self.x >= x2 and self.y >= y2:
                        self.path_pos += 1
                else:  # move up
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
            else: # move left
                if direction[1] >= 0:
                    if self.x <= x2 and self.y >= y2:
                        self.path_pos += 1
                else:
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1
