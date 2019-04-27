import sys
import pygame

from bullet import Bullet


def check_keydown(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it to bullet group
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """Keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(game_settings, screen, ship, bullets):
    """Updates screen image"""
    screen.fill(game_settings.bg_colour)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitship()

    # Update game screen
    pygame.display.flip()
