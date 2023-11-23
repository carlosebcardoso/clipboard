import pygame

class Clip:
    def __init__(self, text):
        self.text = text
        self.rect = pygame.Rect((5, 35, 340, 50))

    def insertClip(self, clipboard):
        clipboard.board.insert(0, self)
        clipboard.organizeClips()

    def scroll(self, direction):
        self.rect.y += direction * 10