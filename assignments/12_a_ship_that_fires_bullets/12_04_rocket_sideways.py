# 12-4, rocket sideways 


import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/12_a_ship_that_fires_bullets/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        new_rect = self.rect.move(dx, dy)
        if self.screen_rect.contains(new_rect):
            self.rect = new_rect

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket Game")
bg_color = (135, 206, 235)  

rocket = Rocket(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        rocket.move(5, 0)
    if keys[pygame.K_UP]:
        rocket.move(0, -5)
    if keys[pygame.K_DOWN]:
        rocket.move(0, 5)

    screen.fill(bg_color)
    rocket.draw()
    pygame.display.flip()
  