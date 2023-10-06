import pygame
# import keyboard
import pyperclip
import threading

pygame.init()

pygame.display.set_caption('Clipboard')
screen = pygame.display.set_mode((350, 585))
icon = pygame.image.load('./clipboard/icon.jpg')
pygame.display.set_icon(icon)

dark_mode_icon = pygame.image.load('./clipboard/dark_mode.svg')
delete_icon = pygame.image.load('./clipboard/delete.svg')

dark_mode_rect = pygame.Rect(5, 5, 24, 24)
delete_rect = pygame.Rect(321, 5, 24, 24)

text_font = pygame.font.SysFont("Helvetica", 16)

clipboard = []

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

def deleteAll():
    for clip in clipboard:
        clipboard.pop()

def organizeClips():
    global clipboard

    for clip in clipboard:
        id = clipboard.index(clip)
        clip['rect'].y = (id*50) + (id*5) + 35

def createClip(text):
    global clipboard
    rect = pygame.Rect((5, 25, 340, 50))

    newClip = {
        'text': text,
        'rect': rect,
    }
    clipboard.insert(0, newClip)
    organizeClips()

firstClip = createClip(pyperclip.paste())

# def openClipBoard():
#     print('open')

# keyboard.add_hotkey('shift+f2', openClipBoard, args=[])

def drawText(text, x, y):
    global text_font
    txt = text_font.render(text, True, txt_color)
    screen.blit(txt, (x, y), (0, 0, 330, 50))
    screen.blit(txt, (x, y), (330, -22, 330, 50))

def addToClipBoard():
    while True:
        clipText = pyperclip.waitForNewPaste()

        for i in clipboard:
            if clipText == i['text']:
                clipboard.remove(i)

        if len(clipboard) >= 10:
            clipboard.pop(9)

        createClip(clipText)

threading.Thread(target=addToClipBoard, daemon=True).start()

run = True
while run:
    screen.fill(bg_color)

    for clip in clipboard:
        pygame.draw.rect(screen, (txt_color), clip['rect'], 2, 2)
        drawText(clip['text'], clip['rect'].x + 5, clip['rect'].y + 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and dark_mode_rect.collidepoint(event.pos):
            switchDarkMode()
        elif event.type == pygame.MOUSEBUTTONDOWN and delete_rect.collidepoint(event.pos):
            deleteAll()
        elif event.type == pygame.MOUSEBUTTONUP:
            for clip in clipboard:
                if clip['rect'].collidepoint(event.pos):
                    pyperclip.copy(clip['text'])

    # delete icon
    pygame.draw.circle(screen, ('white'), (333, 17), 12)
    screen.blit(delete_icon, (delete_rect.x, delete_rect.y))
    # dark mode icon
    pygame.draw.circle(screen, ('white'), (17, 17), 12)
    screen.blit(dark_mode_icon, (5, 5))

    pygame.display.flip()
pygame.quit()
