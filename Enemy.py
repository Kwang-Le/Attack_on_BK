import pygame
from pygame.math import Vector2
import os


class Enemy:
    def __init__(self, pos, waypoints, win):
        self.width = 15
        self.height = 30
        # self.image = pygame.image.load(os.path.join("asset", "sinh_vien.png"))
        # self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.imgs = []
        self.img_num = 0
        self.vel = Vector2(0, 0)
        self.max_speed = 0.4
        self.waypoints = waypoints
        self.waypoints_index = 0
        self.pos = Vector2(pos)
        self.target = self.waypoints[self.waypoints_index]
        self.win = win
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.frame_passed = 0

    def move(self):
        if self.waypoints_index == len(self.waypoints) - 1:
            self.pos = Vector2(self.waypoints[len(self.waypoints)-2])
            self.x = self.pos[0]
            self.y = self.pos[1]
            return
        heading = self.target - self.pos
        distance = heading.length()
        heading.normalize_ip()
        if distance <= 2:
            self.waypoints_index += 1
            self.target = self.waypoints[self.waypoints_index]
        else:
            self.vel = heading * self.max_speed

            self.pos += self.vel
            self.x = self.pos[0]
            self.y = self.pos[1]

    def draw(self):
        if self.frame_passed == 30:
            self.frame_passed = 0
            if self.img_num == 1:
                self.img_num = 0
            else:
                self.img_num = 1
        img = self.imgs[self.img_num]
        draw_pos = (self.x - img.get_width() / 2, self.y - img.get_height() / 2)
        self.win.blit(img, draw_pos)
        self.frame_passed += 1
