import pygame
import os
pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("asset","star.png")),(50,50))#thay đổi nhỏ bé
star2 = pygame.transform.scale(pygame.image.load(os.path.join("asset","star.png")),(10,10))#thay đổi nhỏ bé

tower1_img= pygame.transform.scale(pygame.image.load(os.path.join("asset", "tower1.png")),(50,50))# Menu cho
class Button:
    def __init__(self, x,y ,img,name) :
        self.name =name
        self.img = img
        self.x =x
        self.y =y
        self.width = self.img.get_width()
        self.height= self.img.get_height()

    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw (self,win):
         win.blit(self.img, (self.x,self.y ))

    def update(self):
        """
        updates button position
        :return: None
        """
        self.x -= 50
        self.y -= 110
class PlayPauseButton(Button):
    def __init__(self, play_img,pause_img,x,y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width =  self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self,win):
        if self.paused:
            win.blit(self.play, (self.x,self.y))
        else:
            win.blit(self.pause,(self.x,self.y))


class VerticalButton(Button):
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost
class Menu:
    #menu for holding items:
     def __init__(self,tower, x, y, img, item_cost):
         self.x =x
         self.y =y
         self.width =img.get_width()
         self.height =img.get_height()
         self.item_names =[]
         self.item_cost= item_cost
         self.imgs =[]
         self.items =0
         self.buttons=[]
         self.bg =img   #background
         self.font =pygame.font.SysFont("8-BIT WONDER.TTF",40)
         self.tower=tower


     def add_btn(self, img, name):
         self.items +=1
         inc_x = self.width/self.items/2
         btn_x = self.x -self.bg.get_width()/2   # điều chỉnh upgrade
         btn_y = self.y -120
         self.buttons.append(Button(btn_x, btn_y, img, name))

     def get_item_cost(self):
         return self.item_cost[self.tower.tower.level-1]

     def draw(self, win):
        win.blit(self.bg, (self.x-self.bg.get_width()/2, self.y-120))    #chỗ thay đổi cái upgrade
        for item in self.buttons:
            item.draw(win)
            win.blit(star,(item.x +item.width +10,item.y))
            text =self.font.render(str(self.item_cost[self.tower.level -1]),1,(255,255,255))
            win.blit(text, (item.x +item.width +1,item.y +star.get_height()))      #chỗ thay dổi cái star

     def update(self):
        for btn in self.buttons:
            btn.update()

     def get_clicked(self, X,Y):
         for btn in self.buttons:
             if btn.click(X,Y):
                 return btn.name

         return None


class VerticalMenu(Menu):
        def __init__(self, x, y, img):
            self.x = x
            self.y = y
            self.width = img.get_width()
            self.height = img.get_height()
            self.item_names = []
            self.imgs = []
            self.items = 0
            self.buttons = []
            self.bg = img  # background
            self.font = pygame.font.SysFont("8-BIT WONDER.TTF", 20)   #thay đổi cỡ text chỗ menu
            self.font1 = pygame.font.SysFont("SportypoReguler-OVGwe", 20)  # thay đổi cỡ text chỗ menu


        def add_btn(self, img, name,cost):
            self.items += 1
            #inc_x = self.width / self.items / 2
            btn_x = self.x -40
            btn_y = self.y+100 +(self.items-1)*90 #khoảng cách của side bar
            self.buttons.append(VerticalButton(btn_x, btn_y, img, name,cost))

        def get_item_cost(self, name):
            for btn in self.buttons:
                if btn.name == name:
                    return btn.cost
            return -1

        def draw(self, win):#vẽ mấy cái trụ
            win.blit(self.bg, (self.x -15- self.bg.get_width() / 2, self.y +5))# chỗ thay đổi cái side bar
            SAMI = self.font1.render('SAMI', 1, (0, 255, 255))
            win.blit(SAMI, (1105, 235))
            VLKT = self.font1.render('VLKT', 1, (0, 255, 255))
            win.blit(VLKT, (1105, 325))
            LLCT = self.font1.render('LLCT', 1, (0, 255, 255))
            win.blit(LLCT, (1105, 415))
            for item in self.buttons:
                item.draw(win)
                win.blit(star2, (item.x, item.y+ item.height +5))
                text = self.font.render(str(item.cost), 1, (255, 255, 255))
                win.blit(text, (item.x + item.width/2 -text.get_width()/2 + 1, item.y + item.height +5))  # chỗ thay dổi cái star
