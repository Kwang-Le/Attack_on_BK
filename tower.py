import pygame
import os
import math


class Tower:
    """
    Abstract class for towers
    """
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.range = 200
        self.selected = False
        self.tower_imgs = pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower.png")), (70,70))
        self.damage = 1

        self.place_color = (0,0,255, 100)

    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))
        pygame.display.update()

    def draw_radius(self, win):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        """
        call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level-1]

    def upgrade(self):
        """
        upgrades the tower for a given cost
        :return: None
        """
        pass

    def get_upgrade_cost(self):
        """
        returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level-1]

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True