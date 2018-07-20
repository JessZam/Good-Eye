'''GoodEye - Dickson/Jess/Ryan'''

import pygame, os, sys
from pygame.locals import *
from sys import exit

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
BLUE = (0, 0, 255)
GRAY = (197, 197, 197)
YELLOW = (255, 255, 0)
GREEN = (128, 255, 128)
PURPLE = (128, 255, 128)
RED = (255, 0, 0)
PINK = (255, 170, 255)
ORANGE = (255, 128, 64)
SKY_BLUE = (0, 128, 255)
NAVY_BLUE = (0, 0, 128)
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
                        menu = False
                        game_loop()
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

def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    if n == 0:
        print("Testing")


def game_loop():
    gameExit = False
    gameOver= False
    
    while not gameExit:
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (410, 220, 100, 100))
        pygame.draw.rect(screen, YELLOW, (410, 340, 100, 100))
        pygame.draw.rect(screen, YELLOW, (530, 220, 100, 100))
        pygame.draw.rect(screen, RED, (530, 340, 100, 100))
        '''pygame.draw.rect(screen, PURPLE, (0, 0, 200, 100))
            pygame.draw.rect(screen, PINK, (0, 0, 200, 100))
            pygame.draw.rect(screen, ORANGE, (0, 0, 200, 100))
            pygame.draw.rect(screen, SKY_BLUE, (0, 0, 200, 100))
            pygame.draw.rect(screen, NAVY_BLUE, (0, 0, 200, 100))
            pygame.draw.rect(screen, GRAY, (0, 0, 200, 100))
            '''
        pygame.display.update()
        clock.tick(FPS)



    countdown(30)
    pygame.display.update()
'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(FPS)'''
#Initialize the Game
main_menu()
game_loop()
#pygame.quit()
#quit()
