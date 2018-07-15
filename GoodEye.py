'''GoodEye - Dickson/Jess/Ryan'''

import pygame, os
from pygame.locals import *

pygame.init()

# Game Resolution
screen_width=1000
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GoodEye")
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN_YELLOW = (173,255,47)

font = "freesansbold.ttf"

#------------------------------------------------------------ MAIN MENU --------------------------------------------#

def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(BLACK)
        title=text_format("GoodEye", font, 90, GREEN_YELLOW)
        if selected=="start":
            text_start=text_format("Start", font, 60, GREEN_YELLOW)
        else:
            text_start = text_format("Start", font, 60, WHITE)
        if selected=="quit":
            text_quit=text_format("Quit", font, 60, GREEN_YELLOW)
        else:
            text_quit = text_format("Quit", font, 60, WHITE)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)

#Initialize the Game
main_menu()
pygame.quit()
quit()
