# draw lives
text = self.font_name.render(str(self.lives), 1, (255, 255, 255))
life = pygame.transform.scale(lives_img, (50, 50))
start_x = self.width - life.get_width() - 10

self.win.blit(text, (start_x - text.get_width() - 10, 65))
self.win.blit(life, (start_x, 10))
# draw money
text = self.font_name.render(str(self.money), 1, (255, 255, 255))
money = pygame.transform.scale(star_img, (50, 50))
start_x = self.width - money.get_width() - 10

self.win.blit(text, (start_x - text.get_width() - 10, 65))
self.win.blit(money, (start_x, 10))
