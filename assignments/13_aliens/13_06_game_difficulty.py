# 13-6, game over, pg 313

#Art is made in chatgpt

import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter: Game Over Edition")
clock = pygame.time.Clock()
bg_color = (30, 30, 30)


ship_img = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/ship.png")
alien_img = pygame.image.load("C:/Users/romfu/Desktop/csc_141/assignments/13_aliens/alien.png")

font = pygame.font.SysFont(None, 48)


ship_rect = ship_img.get_rect()
ship_rect.midleft = screen.get_rect().midleft


bullet_color = (255, 255, 0)
bullet_speed = 6
bullets = []


alien_speed = 2
aliens = []


ship_hits = 0
alien_hits = 0
game_active = True


def create_alien_fleet():
    for _ in range(5):
        x = random.randint(700, 780)
        y = random.randint(50, 550)
        rect = alien_img.get_rect()
        rect.topleft = (x, y)
        aliens.append(rect)


def draw_game_over():
    msg = font.render("GAME OVER", True, (255, 0, 0))
    msg_rect = msg.get_rect(center=screen.get_rect().center)
    screen.blit(msg, msg_rect)


create_alien_fleet()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_rect.right, ship_rect.centery - 2, 10, 4)
                bullets.append(bullet)

    if game_active:

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
            elif alien.colliderect(ship_rect):
                aliens.remove(alien)
                ship_hits += 1
                if ship_hits >= 3:
                    game_active = False


        for bullet in bullets[:]:
            for alien in aliens[:]:
                if bullet.colliderect(alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    alien_hits += 1
                    break


        if len(aliens) < 5:
            create_alien_fleet()


    screen.fill(bg_color)
    screen.blit(ship_img, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    for alien in aliens:
        screen.blit(alien_img, alien)

    if not game_active:
        draw_game_over()

    pygame.display.flip()
    clock.tick(60)
