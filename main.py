import pygame
import pyperclip
import threading
# import time
# import keyboard

# pygame and screen init
pygame.init()
pygame.display.set_caption('Clipboard')
screen = pygame.display.set_mode((350, 585))

# global variables
dark_mode_icon = pygame.image.load('dark_mode.svg')
delete_icon = pygame.image.load('delete.svg')

dark_mode_rect = pygame.Rect(5, 5, 24, 24)
delete_rect = pygame.Rect(321, 5, 24, 24)

dark_mode = True
txt_color = 'white'
bg_color = 'black'

def switchDarkMode():
    global dark_mode
    global txt_color
    global bg_color
    
    if dark_mode:
        # switches to light mode
        txt_color = 'black'
        bg_color = 'white'
        dark_mode = False
    else:
        # switches to dark mode
        txt_color = 'white'
        bg_color = 'black'
        dark_mode = True

class Clipboard:
    def __init__(self):
        self.board = []

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

class Clip:
    def __init__(self, text):
        self.text = text
        self.rect = pygame.Rect((5, 25, 340, 50))

    def insertClip(self, clipboard):
        clipboard.board.insert(0, self)
        clipboard.organizeClips()

firstClip = Clip(pyperclip.paste())
firstClip.insertClip(clipboard)

def drawText(text, x, y):
    txt = pygame.font.SysFont("Helvetica", 16).render(text, True, txt_color)
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

        elif event.type == pygame.MOUSEBUTTONDOWN and dark_mode_rect.collidepoint(event.pos):
            switchDarkMode()

        elif event.type == pygame.MOUSEBUTTONDOWN and delete_rect.collidepoint(event.pos):
            clipboard.deleteAll()

        elif event.type == pygame.MOUSEBUTTONUP:
            for clip in clipboard.board:
                if clip.rect.collidepoint(event.pos):
                    pyperclip.copy(clip.text)

    # dark mode icon
    pygame.draw.circle(screen, ('white'), (17, 17), 12)
    screen.blit(dark_mode_icon, (5, 5))
    # delete icon
    pygame.draw.circle(screen, ('white'), (333, 17), 12)
    screen.blit(delete_icon, (delete_rect.x, delete_rect.y))

    pygame.display.flip()
pygame.quit()
