from game import Game
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
#Background
image= pygame.image.load(r'C:\Users\My PC\Downloads\color-seamless-space-pattern_102902-2360.jpg')
screen.blit(image, (0, 0))
#Music
pygame.mixer.music.load(r'C:\Users\My PC\Downloads\Under Pressure - Queen.mp3')
pygame.mixer.music.play(-1)
#Title and Icon
pygame.display.set_caption("Tower Defense")
icon = pygame.image.load(r'C:\Users\My PC\Downloads\tower.png')
pygame.display.set_icon(icon)

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()