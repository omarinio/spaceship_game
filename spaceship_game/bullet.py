import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for bullets the ship fires"""

    def __init__(self, game_settings, screen, ship):
        """Create bullet object"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Initialises position of bullet
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Stores position of bullet as a decimal
        self.y = float(self.rect.y)

        self.colour = game_settings.bullet_colour
        self.speed = game_settings.bullet_speed

    def update(self):
        """Move bullet up the screen"""
        # Update position of bullet
        self.y -= self.speed
        # Update rect of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
