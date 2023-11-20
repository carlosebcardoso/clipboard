import pygame
import pyperclip
import threading
# import time
# import keyboard
from header import Header
from clip import Clip

# pygame and screen init
pygame.init()
pygame.display.set_caption('Clipboard')
screen = pygame.display.set_mode((350, 585))

# global variables
txt_color = 'white'
bg_color = 'black'

header = Header(585)

class Clipboard:
    def __init__(self):
        self.board = []
        self.rect = pygame.Rect(5, 35, 340, 545)

    def addToClipboard(self):
        while True:
            clipText = pyperclip.waitForNewPaste()

            # removes empty
            if self.board[0] == '':
                self.board.pop(0)

            # removes duplicates
            for clip in self.board:
                if clipText == clip.text:
                    self.board.remove(clip)

            # limits clipboard to 10 clips
            if len(self.board) >= 10:
                self.board.pop(-1)

            # creates a new clip with clipText
            newClip = Clip(clipText)
            newClip.insertClip(self)
    
    def organizeClips(self):
        for clip in self.board:
            id = self.board.index(clip)
            clip.rect.y = (id*50) + (id*5) + 35
    
    def deleteAll(self):
        for i in range(len(self.board)):
            self.board.pop()

        firstClip = Clip(pyperclip.paste())
        firstClip.insertClip(self)

clipboard = Clipboard()

firstClip = Clip(pyperclip.paste())
firstClip.insertClip(clipboard)

def drawText(text, x, y):
    txt = pygame.font.SysFont("Helvetica", 16).render(text, True, txt_color)
    if header.hidden.active:
        ast_text = '*' * len(text)
        txt = pygame.font.SysFont("Helvetica", 20).render(ast_text, True, txt_color)
    screen.blit(txt, (x, y), (0, 0, 330, 50))
    screen.blit(txt, (x, y), (330, -22, 330, 50))

threading.Thread(target=clipboard.addToClipboard, daemon=True).start()

run = True
while run:
    screen.fill(bg_color)

    for clip in clipboard.board:
        pygame.draw.rect(screen, (txt_color), clip.rect, 2, 2)
        drawText(clip.text, clip.rect.x + 5, clip.rect.y + 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if header.dark_mode.rect.collidepoint(event.pos):
                txt_color, bg_color = header.dark_mode.switch(txt_color, bg_color)

            elif header.delete.rect.collidepoint(event.pos):
                clipboard.deleteAll()

            elif header.hidden.rect.collidepoint(event.pos):
                header.hidden.active = not header.hidden.active

            elif clipboard.rect.collidepoint(event.pos):
                for clip in clipboard.board:
                    if clip.rect.collidepoint(event.pos):
                        pyperclip.copy(clip.text)

    pygame.draw.rect(screen, 'black', header.rect)
    header.update(screen)

    pygame.display.flip()
pygame.quit()
