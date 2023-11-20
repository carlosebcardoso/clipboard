import pygame
from buttons import *

class Header:
    def __init__(self, screen_width):
        self.rect = pygame.Rect(0, 0, screen_width, 35)

        self.dark_mode = DarkMode()
        self.hidden = Hidden()
        self.delete = Delete()
        self.buttons = [self.dark_mode, self.hidden, self.delete]

    def update(self, screen):
        for button in self.buttons:
            pygame.draw.circle(screen, ('white'), button.circle, button.radius)
            screen.blit(button.icon, button.rect.topleft) 