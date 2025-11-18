# 13-2, better stars, pg 301

#Art is made in chatgpt


import pygame
import sys
from random import randint


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Star Grid")
bg_color = (0, 0, 30)


star_image = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/star.png")
star_rect = star_image.get_rect()


star_width = star_rect.width
star_height = star_rect.height
cols = screen.get_width() // (star_width + 10)
rows = screen.get_height() // (star_height + 10)


stars = []
for row in range(rows):
    for col in range(cols):
        x = col * (star_width + 10) + randint(-10, 10)
        y = row * (star_height + 10) + randint(-10, 10)
        rect = star_rect.copy()
        rect.topleft = (x, y)
        stars.append(rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    for rect in stars:
        screen.blit(star_image, rect)
    pygame.display.flip()
