import pygame
from pygame.math import Vector2
import os


class Enemy():
    def __init__(self, pos, waypoints, win):
        self.width = 15
        self.height = 30
        self.image = pygame.image.load(os.path.join("asset", "sinh_vien.png"))
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        #self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.max_speed = 0.8
        self.waypoints = waypoints
        self.waypoints_index = 0
        self.pos = Vector2(pos)
        self.target = self.waypoints[self.waypoints_index]
        self.win = win
        self.x = self.pos[0]
        self.y = self.pos[1]

    def move(self):
        if self.waypoints_index == len(self.waypoints) - 1:
            self.pos = Vector2(self.waypoints[len(self.waypoints)-2])
            self.x = self.pos[0]
            self.y = self.pos[1]
            #self.rect.center = self.pos
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
            #self.rect.center = self.pos
            self.x = self.pos[0]
            self.y = self.pos[1]

    def draw(self):
        self.win.blit(self.image, (self.x, self.y))
