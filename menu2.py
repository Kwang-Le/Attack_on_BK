import pygame
import os
pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("asset","star.png")),(50,50))#thay đổi nhỏ bé
star2 = pygame.transform.scale(pygame.image.load(os.path.join("asset","star.png")),(10,10))#thay đổi nhỏ bé
class Button:
    def __init__(self,x,y,img,name):
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
         #inc_x = self.width/self.items/2
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

     def get_clicked(self, X,Y):
         for btn in self.buttons:
             if btn.click(X,Y):
                 return btn.game

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


        def add_btn(self, img, name,cost):
            self.items += 1
            #inc_x = self.width / self.items / 2
            btn_x = self.x -40
            btn_y = self.y+80 +(self.items-1)*80 #khoảng cách của side bar
            self.buttons.append(VerticalButton(btn_x, btn_y, img, name,cost))

        def get_item_cost(self):
            return Exception("Not implemented")

        def draw(self, win):#vẽ mấy cái trụ
            win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 120))  # chỗ thay đổi cái side bar
            for item in self.buttons:
                item.draw(win)
                win.blit(star2, (item.x, item.y+ item.height +5))
                text = self.font.render(str(item.cost), 1, (255, 255, 255))
                win.blit(text, (item.x + item.width/2 -text.get_width()/2 + 1, item.y + item.height +5))  # chỗ thay dổi cái star