import pygame
import math
import os

class Enemy:

    def __init__(self, waypoints, win):
        self.width = 15
        self.height = 30
        self.imgs = []
        self.img = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),"asset/Enemy/","Sinhvien0.png")).convert_alpha(), (self.width, self.height))
        self.img_num = 0
        self.path = waypoints #path to go through the map, position of center
        self.path_pos = 0
        self.endpoint = (934, 700)
        self.x = self.path[0][0] # first x and y of enemy
        self.y = self.path[0][1]
        self.max_health = 100
        self.current_health = 1
        self.init_speed = 0.4
        self.speed = 0
        self.frame_passed = 0
        self.win = win
        self.is_flipped = False
        self.exp_imgs = []
        self.exp_imgs_num = 0
        self.add_exp_imgs()
        self.frame_passed = 0

    def draw_images(self):
        """Draw enemies' animations hihi.
        win: game surface."""
        self.img = self.imgs[self.img_num]
        draw_pos = (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2)
        self.win.blit(self.img, draw_pos)
        self.draw_health_bar()

    def draw_health_bar(self):
        """Draw enemies' health bar hihi.
        win: game surface."""
        green = (0,255,0)
        red = (255,0,0)
        draw_pos = (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 4)
        max_health = pygame.draw.rect(self.win, red, pygame.Rect(draw_pos,(self.width + 1, 2)))
        current_health = pygame.draw.rect(self.win, green, pygame.Rect(draw_pos,((self.width + 1)*(self.current_health/self.max_health), 2)))

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

    def add_exp_imgs(self):
        for i in range(6):
            self.exp_imgs.append(pygame.transform.scale(pygame.image.load(
                os.path.join(os.path.dirname(os.path.dirname(__file__)), "asset/explosion/",
                             "explosion" + str(i) + ".png")).convert_alpha(), (50,50)))

    def draw_explosion(self, x, y):
        """ Draw explosion at the position enemy died."""
        self.frame_passed += 1
        img = self.exp_imgs[self.exp_imgs_num]
        draw_pos = (x - img.get_width() / 2, y - img.get_height() / 2)
        self.win.blit(img, draw_pos)
        if self.frame_passed % 5 == 0:
            if self.exp_imgs_num <= 4:
                self.exp_imgs_num += 1

    def flip(self):
        """Flip images."""
        self.img = pygame.transform.flip(self.img, True, False)

    def move(self):
        """Moves enemy."""
        self.frame_passed += 1
        if self.frame_passed == 30:
            self.img_num += 1
            if self.img_num >= len(self.imgs):
                self.img_num = 0
            self.frame_passed = 0

        if self.path_pos < len(self.path):
            x1, y1 = self.path[self.path_pos]
            if self.path_pos == len(self.path) - 1:
                x2, y2 = self.endpoint
            else:
                x2, y2 = self.path[self.path_pos + 1]

            length = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
            direction = ((x2 - x1)/length * self.speed, (y2 - y1)/length * self.speed)
            self.x, self.y = (self.x + direction[0], self.y + direction[1])

            if direction[0] > 0 and not (self.is_flipped):
                self.is_flipped = True
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)
            elif direction[0] < 0 and (self.is_flipped):
                self.is_flipped = False
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)

            if direction[0] >= 0: #move right
                if direction[1] >= 0: #move down
                    if self.x >= x2 and self.y >= y2:
                        self.path_pos += 1
                else:  # move up
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
            else: # move left
                self.is_flipped = False
                if direction[1] >= 0:
                    if self.x <= x2 and self.y >= y2:
                        self.path_pos += 1
                else:
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1

