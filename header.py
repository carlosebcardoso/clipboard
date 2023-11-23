import pygame
from buttons import *

class Header:
    def __init__(self, screen_width):
        self.rect = pygame.Rect(0, 0, screen_width, 35)

        self.dark_mode = DarkMode()
        self.hidden = Hidden()
        self.delete = Delete()
        self.debug = Debug()
        self.buttons = [self.dark_mode, self.hidden, self.delete, self.debug]

    def update(self, screen, bg_color):
        pygame.draw.rect(screen, bg_color, self.rect)
        for button in self.buttons:
            pygame.draw.circle(screen, ('white'), button.circle, button.radius)
            screen.blit(button.icon, button.rect.topleft) 