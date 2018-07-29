'''GoodEye - Dickson/Jess/Ryan'''

import pygame, os, sys
from pygame.locals import *
from sys import exit
from PyQt5 import QtWidgets

pygame.init()
gameExit = False #for switches
gameOver = False #for switches


#------------------------------------------ Declarations -----------------------------------------------------------#
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GoodEye")
clock = pygame.time.Clock()
FPS = 30

#--------------------------------------- Declarations ENDS ---------------------------------------------------------#



#------------------------------------------- Text Renderer ------------------------------------------------------------#
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

#------------------------------------------- Text Renderer ENDS -------------------------------------------------------#



#----------------------------------------------- Colors ---------------------------------------------------------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN_YELLOW = (173, 255, 47)
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

#----------------------------------------------- Colors ENDS ----------------------------------------------------------#




#--------------------------------------------------- MAIN MENU --------------------------------------------------------#

def main_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        menu = False
                        game_loop()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(BLACK)
        title = text_format("GoodEye", font, 90, GREEN_YELLOW)
        if selected == "start":
            text_start = text_format("Start", font, 60, GREEN_YELLOW)
        else:
            text_start = text_format("Start", font, 60, WHITE)
        if selected == "quit":
            text_quit = text_format("Quit", font, 60, GREEN_YELLOW)
        else:
            text_quit = text_format("Quit", font, 60, WHITE)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)

#---------------------------------------------- MAIN MENU ENDS -------------------------------------------------------#



#-------------------------------------------- CountDown Timer ---------------------------------------------------------#
#------Code Inspired by https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame uploaded by Sloth-------#
def countdown(time):

    count,text = time, str(time).rjust(10)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('bold', 50)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.USEREVENT:
                    count -= 1
                    text = str(count).rjust(10) \
            if count > 0 else "GAMEOVER."

        else:
            Rect = pygame.draw.rect(screen, BLACK, (380, 50, 250, 60))
            screen.blit(font.render(text, True, (255, 255, 255)), (405, 60))
            pygame.display.flip()
            pygame.display.update(Rect)
            clock.tick(FPS)
            continue



#-------------------------------------------- CountDown Timer ENDS ----------------------------------------------------#



#---------------------------------------------- Game Mechanics --------------------------------------------------------#

def game_loop():
    gameExit = False
    gameOver = False
    while not gameExit:
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (410, 220, 100, 100))
        pygame.draw.rect(screen, YELLOW, (410, 340, 100, 100))
        pygame.draw.rect(screen, YELLOW, (530, 220, 100, 100))
        pygame.draw.rect(screen, RED, (530, 340, 100, 100))

        #mulitple if statements to control time per level
        #example counter will be the variable to change for each level
        # if count ==1:
        #   time = 20;

        time = 10

        clock.tick(FPS)
        countdown(time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()






#---------------------------------------------- Game Mechanics ENDS ---------------------------------------------------#

# Initialize the Game
main_menu()
game_loop()
quit()
