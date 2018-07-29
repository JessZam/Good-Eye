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
    # Every global variable needs to be referenced
    global clock
    menu=True
    selected="start"

    start_blit = None       # Declare variables before assignment
    quit_blit = None

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    # Use collision enabled objects to figure which of the 2 buttons were clicked
                    if start_blit.collidepoint(event.pos):
                        print("Collision Start")
                        selected = "start"
                        menu = False

                    elif quit_blit.collidepoint(event.pos):
                        print("Collision quit")
                        selected = "quit"
                        pygame.quit()
                        quit()
                elif event.button==1:
                    selected="quit"
                    if quit_blit.collidepoint(event.pos):
                        print("Collision quit")


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
        start_blit = screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))     # Variable now tracks collision
        quit_blit = screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)

    # Main game loop
    game_loop()



# Draws rectangles dynamically, depending on the data passed
def drawRect(rects, founds, colors, temp, n):
    global screen
    rect = None

    # Override display if color found or user is checking the value (1 and 2 clicks)
    if founds[n] != None or temp[n] != None:
        rect = pygame.draw.rect(screen, colors[n], rects[n])
    else:
        rect = pygame.draw.rect(screen, GRAY, rects[n])


    return rect



def game_loop():
    gameExit = False
    gameOver= False
    gameStarts = False          # Game starts
    gamePause = False           # Game pause

    initialTimer = 10     # Initial time for game to start

    lives = 5           # 5 lives total


    x = None            # x mouse position
    y = None            # y mouse position

    clicked = 0         # counts mouse clicks

    level = 1   # levels are signaled by a variable

    # Algebra rectangles where to draw on different levels
    rects_1 = [(410, 220, 100, 100),(410, 340, 100, 100), (530, 220, 100, 100), (530, 340, 100, 100)]
    rects_2 = rects_1 + [(410, 100, 100, 100),(530, 100, 100, 100)]

    # Colors
    colors_1 = [RED, YELLOW, YELLOW, RED]
    colors_2 = [RED, YELLOW, YELLOW, RED, NAVY_BLUE, NAVY_BLUE]

    # Collision detection variables: PyGame includes collision detection with rectangles
    collision_1 = [None, None, None, None]
    collision_2 = [None, None, None, None, None, None]

    # Parallel lists for finding elements
    found_1 = [None, None, None, None]
    found_2 = [None, None, None, None, None, None]

    # Parallel lists for temporary clicks - reset if clicks 2
    temp_1 = [True, True, True, True]
    temp_2 = [True, True, True, True, True, True]

    wins_1 = [[0,3],[1,2]]              # Lists hold the winning combinations
    wins_2 = wins_1 + [[4,5]]


    currentTicks = 0        # Calls functions 1 per second (accumulates ticks)

    while not gameExit:
        screen.fill(WHITE)

        # Display screen depending on the level
        if level == 1:
            collision_1[0] = drawRect(rects_1, found_1, colors_1, temp_1, 0)
            collision_1[1] = drawRect(rects_1, found_1, colors_1, temp_1, 1)
            collision_1[2] = drawRect(rects_1, found_1, colors_1, temp_1, 2)
            collision_1[3] = drawRect(rects_1, found_1, colors_1, temp_1, 3)

        elif level == 2:
            collision_2[0] = drawRect(rects_2, found_2, colors_2, temp_2, 0)
            collision_2[1] = drawRect(rects_2, found_2, colors_2, temp_2, 1)
            collision_2[2] = drawRect(rects_2, found_2, colors_2, temp_2, 2)
            collision_2[3] = drawRect(rects_2, found_2, colors_2, temp_2, 3)
            collision_2[4] = drawRect(rects_2, found_2, colors_2, temp_2, 4)
            collision_2[5] = drawRect(rects_2, found_2, colors_2, temp_2, 5)




        # Timer text
        timerText = text_format(str(initialTimer), font, 60, GREEN_YELLOW)

        # Live text
        livesText = text_format('Lives='+str(lives), font, 60, RED)

        # Runs timer 1 per second
        if gameStarts == False:
            if initialTimer != 0:
                screen.blit(timerText, (screen_width / 2 - (screen_height / 2), 300))
            else:
                # Game starts
                gameStarts = True
                found_1 = [None, None, None, None]
                found_2 = [None, None, None, None, None, None]

                # Set temporary to None so that there is no more showing of textures
                temp_1 = [None, None, None, None]
                temp_2 = [None, None, None, None, None, None]


        else:
            screen.blit(livesText, (100 , 100))   # Display lives

            if initialTimer == 0 and clicked == 2:
                temp_1 = [None, None, None, None]
                temp_2 = [None, None, None, None, None, None]

                clicked = 0

        # After draw, check event
        for event in pygame.event.get():
            if event.type == QUIT:
                gameExit = True
            elif event.type == MOUSEBUTTONDOWN:

                # Only play game is not pause
                if gameStarts == True:
                    if level == 1:
                        # Enumerate means index and value, it is a common practice in python
                        for i,item in enumerate(collision_1):
                            # Check if mouse click occurred inside item
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_1[i] != True:

                                    clicked += 1  # Always increase counter of clicks if click valid

                                    temp_1[i] = True        # Temporary record which rectangle was clicked

                                    if clicked == 2:

                                        two_clicks = [i for i,v in enumerate(temp_1) if v is not None]
                                        if two_clicks in wins_1:
                                            for i in two_clicks:
                                                found_1[i] = True

                                            # Find out if win
                                            totalWins = sum([1 for i in found_1 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_1):
                                                print('Victory')
                                                level = 2

                                                # Reset all values to start on level 2
                                                temp_2 = [True, True, True, True, True, True]

                                                lives = 5               # Set lives back to 5

                                                gameStarts = False

                                                initialTimer = 10       # Set timer back to 10

                                                continue            # Jump to next iteration


                                            temp_1 = [None, None, None, None]
                                        else:
                                            lives -= 1          # Subtract lives

                                            initialTimer = 1    # Set timer to give time to look at different matches (otherwise is instant)



                    else:
                        for i,item in enumerate(collision_2):
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_2[i] != True:

                                    clicked += 1  # Always increase counter of clicks if click valid

                                    temp_2[i] = True  # Temporary record which rectangle was clicked

                                    if clicked == 2:

                                        two_clicks = [i for i, v in enumerate(temp_2) if v is not None]
                                        if two_clicks in wins_2:
                                            for i in two_clicks:
                                                found_2[i] = True
                                            # Find out if win
                                            totalWins = sum([1 for i in found_2 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_2):
                                                print('Victory')
                                            temp_2 = [None, None, None, None, None, None]
                                        else:
                                            lives -= 1  # Subtract lives

                                            initialTimer = 1  # Set timer to give time to look at different matches (otherwise is instant)

        # Reduce timer only if game has not start
        if currentTicks == 0:
            if initialTimer > 0:
                initialTimer -= 1  # Count down
        if currentTicks == FPS:
            currentTicks = 0  # Counts ticks once per second
        else:
            currentTicks += 1  # Increase ticks if mark not at FPS (that is if number is not 30)

        pygame.display.update()
        clock.tick(FPS)




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

#pygame.quit()
#quit()
