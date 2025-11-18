# 13-4, steady rain, pg 304

#Art is made in chatgpt


import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Steady Rain")
bg_color = (0, 0, 30)


raindrop_image = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/raindrop.png")
raindrop_rect = raindrop_image.get_rect()


drop_width = raindrop_rect.width
drop_height = raindrop_rect.height
cols = screen.get_width() // (drop_width + 10)


raindrops = []
for row in range(6): 
    for col in range(cols):
        x = col * (drop_width + 10)
        y = row * (drop_height + 10)
        rect = raindrop_rect.copy()
        rect.topleft = (x, y)
        raindrops.append(rect)


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    for drop in raindrops[:]:
        drop.y += 2
        if drop.top > screen.get_height():
            raindrops.remove(drop)


    if len(raindrops) < cols * 6:
        for col in range(cols):
            x = col * (drop_width + 10)
            y = -drop_height  
            rect = raindrop_rect.copy()
            rect.topleft = (x, y)
            raindrops.append(rect)


    screen.fill(bg_color)
    for drop in raindrops:
        screen.blit(raindrop_image, drop)
    pygame.display.flip()
    clock.tick(60)
