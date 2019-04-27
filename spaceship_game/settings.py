class Settings():
    """Class storing all settings for the game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (174, 232, 246)

        self.ship_speed = 1

        # Bullet Settings
        self.bullet_speed = 0.75
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_colour = (60, 60, 60)
