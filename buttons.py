import pygame

class Button:
    def __init__(self, x, path):
        self.radius = 12
        self.rect = pygame.Rect(x, 5, self.radius*2, self.radius*2)
        self.icon = pygame.image.load(path)
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
        super().__init__(39, 'hidden.svg')
        self.active = False

class Delete(Button):
    def __init__(self):
        super().__init__(321, 'delete.svg')
