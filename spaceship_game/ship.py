import pygame


class Ship():

    def __init__(self, game_settings, screen):
        """Initialise the ship and its starting position"""
        self.screen = screen
        self.game_settings = game_settings

        # Load spaceship
        self.image = pygame.image.load('images\spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each ship starts at the canter and bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position depending on flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed

        self.rect.centerx = self.center

    def blitship(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
