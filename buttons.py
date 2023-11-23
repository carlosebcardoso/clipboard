import pygame
import pyperclip
import time
# from clip import Clip

class Button:
    def __init__(self, x, path):
        self.radius = 12
        self.rect = pygame.Rect(x, 5, self.radius*2, self.radius*2)
        self.icons_folder = '_internal/icons/'
        self.icon = pygame.image.load(self.icons_folder + path)
        self.circle = (self.rect.x + self.radius, self.rect.y + self.radius)

class DarkMode(Button):
    def __init__(self):
        super().__init__(5, 'dark_mode.svg')
        self.active = True

    def switch(self, txt_color, bg_color):
        if self.active:
            # switches to light mode
            txt_color = 'black'
            bg_color = 'white'
            self.active = False
        else:
            # switches to dark mode
            txt_color = 'white'
            bg_color = 'black'
            self.active = True

        return (txt_color, bg_color)

class Hidden(Button):
    def __init__(self):
        super().__init__(39, 'visible.svg')
        self.active = False

    def change_icon(self):
        if self.active:
            self.icon = pygame.image.load(self.icons_folder + 'hidden.svg')
        else:
            self.icon = pygame.image.load(self.icons_folder + 'visible.svg')

class Delete(Button):
    def __init__(self):
        super().__init__(321, 'delete.svg')

class Debug(Button):
    def __init__(self):
        super().__init__(321 - 34, 'debug.svg')

    def fill_clipboard(self):
        for i in range(0, 10):
            pyperclip.copy(i)
            time.sleep(0.02)
