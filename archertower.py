import pygame
from tower import Tower
import os
import math
from Enemy.enemy import Enemy
from menu2 import Menu

menu_bg= pygame.transform.scale(pygame.image.load(os.path.join("asset", "menu.png")),(120,70))
upgrade_btn= pygame.transform.scale(pygame.image.load(os.path.join("asset", "upgrade.png")),(50,50))


tower_imgs1 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower1.png")),(50, 50))
tower_imgs2 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower2.png")),(50, 50))
tower_imgs3 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower3.png")),(50, 50))
tower_imgs4 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower4.png")),(50, 50))
archer_imgs1 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "archer1.png")),(50, 50))
archer_imgs2 = pygame.transform.scale(pygame.image.load(os.path.join("asset", "archer2.png")),(50, 50))
archer_imgs = [archer_imgs1, archer_imgs2]
tower_imgs = [tower_imgs1]
class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 100
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "archer"
        self.dead_enemy = []
        self.dead_enemy_pos = []
        self.menu2 = Menu(self, self.x, self.y, menu_bg, [2000, 5000, "MAX"])  # tăng cái upgrade lên max
        self.menu2.add_btn(upgrade_btn, ("Upgrade"))

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        pass

    def draw(self, win):
        """
        draw the arhcer tower and animated archer
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs)*20:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count//20]
        if self.left == True:
            add = -25
        else:
            add = -archer.get_width() + 10
        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            dis = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)
        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 30:
                if Enemy.is_hit(first_enemy, first_enemy.x, first_enemy.y) == True:
                    Enemy.damage(first_enemy, 100)
                    money = first_enemy.money * 2
                    if first_enemy.dead() and len(enemies) > 0:
                        self.dead_enemy_pos.append((first_enemy.x, first_enemy.y))
                        self.dead_enemy.append(first_enemy)
                        enemies.remove(first_enemy)
                        pygame.mixer.music.load("05.mp3")
                        pygame.mixer.music.play()

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
        for i in range(len(self.dead_enemy)):
            self.dead_enemy[i].draw_explosion(self.dead_enemy_pos[i][0], self.dead_enemy_pos[i][1])
        return money

class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs2
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 120
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage
        self.name = "archer2"

    def get_upgrade_cost(self):
        return self.menu2.get_item_cost()

        self.menu = Menu(self, self.x, self.y, menu_bg, [2500, 5500, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer2"
        pass

class Slow(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs3
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "slow"
        self.slow = 0
        self.dead_enemy = []
        self.dead_enemy_pos = []

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        pass

    def draw(self, win):
        """
        draw the arhcer tower and animated archer
        :param win: surface
        :return: int
        """

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs)*20:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count//20]
        if self.left == True:
            add = -25
        else:
            add = -archer.get_width() + 25
        win.blit(archer, ((self.x + add), (self.y - 25)))
        super().draw_radius(win)
        super().draw(win)

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            dis = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
            if dis < self.range:
                self.inRange = True
                enemy.slow()
                enemy_closest.append(enemy)
            if dis > self.range:
                enemy.un_slow()
        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[-1]
            if self.archer_count == 30:
                if Enemy.is_hit(first_enemy, first_enemy.x, first_enemy.y) == True:
                    Enemy.damage(first_enemy, 100)
                    money = first_enemy.money * 2
                    if first_enemy.dead():
                        self.dead_enemy_pos.append((first_enemy.x, first_enemy.y))
                        self.dead_enemy.append(first_enemy)
                        enemies.remove(first_enemy)
                        # self.slow = 0
                        pygame.mixer.music.load("05.mp3")
                        pygame.mixer.music.play()

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
        for i in range(len(self.dead_enemy)):
            self.dead_enemy[i].draw_explosion(self.dead_enemy_pos[i][0], self.dead_enemy_pos[i][1])
        return money