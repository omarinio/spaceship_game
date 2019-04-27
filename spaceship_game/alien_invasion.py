import pygame

from settings import Settings
from ship import Ship
import game as g
from pygame.sprite import Group


def run_game():
	# Initialise game and create screen
	pygame.init()
	game_settings = Settings()

	screen = pygame.display.set_mode((game_settings.screen_width,
									  game_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")
	# Makes a ship
	ship = Ship(game_settings, screen)
	# Makes a bullet group
	bullets = Group()

	# Main game loop
	while True:
		g.check_events(game_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		g.update_screen(game_settings, screen, ship, bullets)


run_game()
