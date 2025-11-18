# 13-5, sidescrolling, pg 308

#Art is made in chatgpt


import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter Part 2")
clock = pygame.time.Clock()
bg_color = (30, 30, 30)


ship_img = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/ship.png")
alien_img = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/alien.png")


ship_rect = ship_img.get_rect()
ship_rect.midleft = screen.get_rect().midleft


bullet_color = (255, 255, 0)
bullet_speed = 6
bullets = []


alien_speed = 2
aliens = []


def create_alien_fleet():
    for i in range(5):
        x = random.randint(700, 780)
        y = random.randint(50, 550)
        rect = alien_img.get_rect()
        rect.topleft = (x, y)
        aliens.append(rect)

create_alien_fleet()


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


    for alien in aliens[:]:
        alien.x -= alien_speed
        if alien.right < 0:
            aliens.remove(alien)


    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                break


    if len(aliens) < 5:
        create_alien_fleet()


    screen.fill(bg_color)
    screen.blit(ship_img, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    for alien in aliens:
        screen.blit(alien_img, alien)
    pygame.display.flip()
    clock.tick(60)
