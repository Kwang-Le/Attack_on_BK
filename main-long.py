import pygame
from menu import *

# from pygame.math import Vector2
import os
# from Enemy import Enemy
from Enemy.SInh_vien import Sinh_vien
from Enemy.San_BK import San_BK
from archertower import ArcherTowerLong,ArcherTowerShort, Slow
from menu2 import VerticalMenu, PlayPauseButton
import random
pygame.font.init()

pygame.init()
win = pygame.display.set_mode((800, 450))
menu_bg= pygame.transform.scale(pygame.image.load(os.path.join("asset", "menu.png")),(120,70))
upgrade_btn= pygame.transform.scale(pygame.image.load(os.path.join("asset", "upgrade.png")),(50,50))
star_img =pygame.transform.scale(pygame.image.load(os.path.join("asset", "star.png")),(50,50))
lives_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "heart.png")),(40,50))
side_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "sidebar2.png")),(60,420))# Menu cho

play_btn= pygame.transform.scale(pygame.image.load(os.path.join("asset", "continue.png")),(50,50))
pause_btn= pygame.transform.scale(pygame.image.load(os.path.join("asset", "pause.png")),(50,50))

stop_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "stop.png")),(300,300))# Menu cho

tower1_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower1.png")),(50,50))# Menu cho
tower2_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower2.png")),(50,50))# Menu cho
tower3_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower3.png")),(50,50))# Menu cho

attack_tower_names = ["archer", "archer2", "slow"]
class Game:
    def __init__(self):#Các lệnh cơ bản
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.width = 1200
        self.height = 600
        self.display = pygame.Surface((self.width,self.height))
        self.window = pygame.display.set_mode(((self.width,self.height)))
        self.font_name = r'8-BIT WONDER.TTF'
        self.life_font = pygame.font.SysFont("comicsans", 65)
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.waypoints = [(32, 295), (931, 294), (934, 650)]
        self.waypoints2 = [(652, 9), (654, 293), (933, 297), (932, 594)]
        self.bg = pygame.image.load(os.path.join("asset", "BK_map.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.enemies = []
        self.despawn = []
        self.win = win
        self.game_running = True
        self.last_spawn = 0
        self.towers=[]
        self.selected_tower =None
        self.money=2000
        self.lives=100
        self.menu2= VerticalMenu(self.width -side_img.get_width() - 5,150,side_img)  #Thay đổi tọa độ của side bar
        self.menu2.add_btn(tower1_img, "tower1", 500)
        self.menu2.add_btn(tower2_img, "tower2", 500)
        self.menu2.add_btn(tower3_img, "tower3", 500)

        self.attack_towers=[]
        self.support_towers=[]
        self.moving_object = None
        self.pause=True
        self.playPauseButton = PlayPauseButton(play_btn,pause_btn,10, self.height-85)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            pygame.mixer.music.stop()
            self.run()
            # self.display.fill(self.BLACK)
            # self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            # self.window.blit(self.display, (0,0))
            #pygame.display.update()
            self.reset_keys()

    def run(self):
        clock = pygame.time.Clock()
        run = True
        interval = 0
        while self.game_running:
            clock.tick(60)
            waypoints = random.choice([self.waypoints1, self.waypoints2])

            pos = pygame.mouse.get_pos()
            # move moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
            # check game events
            self.check_events()
            now = pygame.time.get_ticks()
            # random spawning
            if now - self.last_spawn > interval:
                self.last_spawn = now
                self.enemies.append(random.choice([Sinh_vien(waypoints, win),San_BK(waypoints, win)]))
                interval = random.choice([1000, 2000, 3000, 4000, 5000])
            # draw everything
            self.draw()
            for point in self.waypoints:
                pygame.draw.rect(win, (90, 200, 40), (point, (4, 4)))
                # loop through enemies
                # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.despawn:
                    en.move()
                    if en.x < -15:
                        to_del.append(en)

                # generate enemies
                for enemy in self.enemies:
                    enemy.move()
                    enemy.draw_images()
                    if enemy.y > 600:
                        self.lives -= 1
                        self.despawn.append(enemy)
                # despawn enemies
                for d in self.despawn:
                    self.despawn.remove(d)
                for t in self.towers:
                    self.money += t.attack(self.enemies)
                    t.draw(self.win)
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        win.blit(self.bg, (0, 0))
        # win.fill((255, 255, 255))
        # pygame.display.set_caption("Attack_on_BK")
        for click in self.clicks:
            pygame.draw.circle(win, (255,0,0), (click[0],click[1]), 5,0)
        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)
        #draw menu
        self.menu2.draw(self.win)
        #draw play and pause button
        self.playPauseButton.draw(self.win)
        #draw stop
        if self.pause:
            screen.blit(stop_img, (480, 100))
        if not self.pause:
            pygame.mixer.music.load("song stop.mp3")
            pygame.mixer.music.play(-1)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255, 0, 0))
        life = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))
        # draw money
        text = self.life_font.render(str(self.money), 1, (0, 0, 255))
        money = pygame.transform.scale(star_img, (50, 50))
        start_x = self.width - money.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        # generate waypoints(not for production)
        # for point in self.waypoints:
            # pygame.draw.rect(win, (90, 200, 40), (point, (4, 4)))

        # generate enemies
        despawn = []
        for enemy in self.enemies:
            enemy.move()
            enemy.draw_images()
            if enemy.y > 600:
                despawn.append(enemy)

        # despawn enemies
        for d in despawn:
            self.enemies.remove(d)
            self.lives -= 1

        # generate towers
        for t in self.towers:
            self.money += t.attack(self.enemies)
            t.draw(self.win)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.game_running = False, False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # self.clicks.append(pos)
                # check moving object
                if self.moving_object:
                    print(self.moving_object.name)
                    if self.moving_object.name in attack_tower_names:
                        self.towers.append(self.moving_object)
                    self.moving_object.moving = False
                    self.moving_object = None

                # print(self.clicks)
                else:
                    #check if click on play or pause
                    if self.playPauseButton.click(pos[0],pos[1]):
                        print("run")
                        self.pause =not(self.pause)
                        self.playPauseButton.paused=self.pause

                    # check if click on side menu
                    side_menu_button = self.menu2.get_clicked(pos[0], pos[1])
                    if side_menu_button:
                        cost = self.menu2.get_item_cost(side_menu_button)
                        if self.money >= cost:
                            self.money -= cost
                            self.add_tower(side_menu_button)
                            print(side_menu_button)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["tower1", "tower2", "tower3", "tower4"]
        object_list = [ArcherTowerLong(x, y),ArcherTowerShort(x,y), Slow(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

screen = pygame.display.set_mode((500, 500))
#Background
#image= pygame.image.load(r'C:\Users\My PC\Downloads\color-seamless-space-pattern_102902-2360.jpg')
image = pygame.Surface((500,500))
image.fill('black')
screen.blit(image, (0, 0))
#Music
pygame.mixer.music.load("Under Pressure - Queen.mp3")
pygame.mixer.music.play(-1)
#Title and Icon
pygame.display.set_caption("Tower Defense")
icon = pygame.image.load('tower.png')
pygame.display.set_icon(icon)

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

