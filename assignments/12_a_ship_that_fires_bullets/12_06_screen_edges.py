# 12-6, sideways shooter, pg 291


import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")
bg_color = (30, 30, 30)

ship_image = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/12_a_ship_that_fires_bullets/ship.bmp")
ship_rect = ship_image.get_rect()
ship_rect.midleft = screen.get_rect().midleft

bullet_color = (255, 255, 0)
bullet_speed = 5
bullets = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_rect.right, ship_rect.centery - 2, 10, 4)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= 5
    if keys[pygame.K_DOWN] and ship_rect.bottom < screen.get_height():
        ship_rect.y += 5

    for bullet in bullets[:]:
        bullet.x += bullet_speed
        if bullet.left > screen.get_width():
            bullets.remove(bullet)

    screen.fill(bg_color)
    screen.blit(ship_image, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    pygame.display.flip()

    clock.tick(60)
