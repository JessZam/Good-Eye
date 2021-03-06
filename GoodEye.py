'''GoodEye - Dickson/Jess/Ryan'''

import pygame, os, sys
from pygame.locals import *
from sys import exit

pygame.init()

# Game Resolution

screen_width=1000
screen_height=1000
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
GREEN_YELLOW = (124,252,0)
BLUE = (0, 0, 255)
DGRAY = (96,96,96)
YELLOW = (255,255,0)
LIME = (0, 255, 0)
PURPLE = (102,0,204)
RED = (255, 0, 0)
SALMON = (255,102,102)
PINK = (255, 20, 147)
ORANGE = (255, 100, 0)
CYAN = (0,255,255)
BABYBLUE =(51,153,255)
OLIVE = (153,153,0)
GRAY = (197, 197, 197)

font = "freesansbold.ttf"
#pygame.mixer.music.play(0)
correct = "Correct.mp3"
incorrect = "Incorrect.mp3"

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
                        selected = "start"
                        menu = False

                    elif quit_blit.collidepoint(event.pos):
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
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 90))
        start_blit = screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 400))     # Variable now tracks collision
        quit_blit = screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 460))
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
    count = 0
    initialTimer = 3     # Initial time for game to start
    lives = 5

    x = None            # x mouse position
    y = None            # y mouse position

    clicked = 0         # counts mouse clicks

    level = 1   # levels are signaled by a variable
    # Algebra rectangles where to draw on different levels
    rects_1 = [(410, 220, 100, 100),(410, 340, 100, 100), (530, 220, 100, 100), (530, 340, 100, 100)]
    rects_2 = rects_1 + [(290, 220, 100, 100),(290, 340, 100, 100),(650, 220, 100, 100),(650, 340, 100, 100)]
    rects_3 = rects_2 + [(290,460,100,100),(410,460,100,100),(530,460,100,100),(650,460,100,100)]
    rects_4 = rects_3 + [(290,580,100,100),(410,580,100,100),(530,580,100,100),(650,580,100,100)]
    rects_5 = rects_4 + [[170,220,100,100],(170,340,100,100),(170,460,100,100),(170,580,100,100),(770,220,100,100),(770,340,100,100),(770,460,100,100),(770,580,100,100)]

    # Colors
    colors_1 = [RED, YELLOW, YELLOW, RED]
    colors_2 = [GREEN_YELLOW,BLUE,YELLOW,RED,RED,YELLOW,BLUE,GREEN_YELLOW]
    colors_3  = [BLUE,GREEN_YELLOW,GREEN_YELLOW,ORANGE,ORANGE,PINK,YELLOW,RED,RED,BLUE,YELLOW,PINK]
    colors_4 = [RED, YELLOW, PURPLE, RED, ORANGE, BLUE, BLUE, GREEN_YELLOW, GREEN_YELLOW, YELLOW, CYAN, WHITE,WHITE , PURPLE, ORANGE, CYAN]
    colors_5 = [PINK,ORANGE,CYAN,YELLOW,GREEN_YELLOW,BABYBLUE,DGRAY,BLUE,DGRAY,BLUE,PINK,RED,PURPLE,WHITE,GREEN_YELLOW,CYAN,WHITE,PURPLE,
    SALMON,YELLOW,SALMON,RED,ORANGE,BABYBLUE]

    # Collision detection variables: PyGame includes collision detection with rectangles

    collision_1 = [None, None, None, None]
    collision_2 = [None, None, None, None, None, None, None, None]
    collision_3 = [None, None, None, None, None, None, None, None, None, None, None, None]
    collision_4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    collision_5 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    # Parallel lists for finding elements
    found_1 = [None, None, None, None]
    found_2 = [None, None, None, None, None, None, None, None]
    found_3 = [None, None, None, None, None, None, None, None,None,None,None,None]
    found_4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    found_5 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    # Parallel lists for temporary clicks - reset if clicks 2
    temp_1 = [True, True, True, True]
    temp_2 = [True, True, True, True, True, True, True, True]
    temp_3 = [True, True, True, True, True, True, True, True,True,True,True,True]
    temp_4 = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    temp_5 = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

    wins_1 = [[0,3],[1,2]]              # Lists hold the winning combinations
    wins_2 = [[0,7],[1,6],[3,4],[2,5]]
    wins_3 = [[0,9],[1,2],[3,4],[5,11],[6,10],[7,8]]
    wins_4 = [[0,3],[1,9],[2,13],[4,14],[5,6],[7,8],[10,15],[11,12]]
    wins_5 = [[0,10],[1,22],[2,15],[3,19],[4,14],[5,23],[6,8],[7,9],[11,21],[12,17],[13,16],[18,20]]

    currentTicks = 0        # Calls functions 1 per second (accumulates ticks)

    while not gameExit:
        screen.fill(BLACK)
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
            collision_2[6] = drawRect(rects_2, found_2, colors_2, temp_2, 6)
            collision_2[7] = drawRect(rects_2, found_2, colors_2, temp_2, 7)

        elif level == 3:
            collision_3[0] = drawRect(rects_3, found_3, colors_3, temp_3, 0)
            collision_3[1] = drawRect(rects_3, found_3, colors_3, temp_3, 1)
            collision_3[2] = drawRect(rects_3, found_3, colors_3, temp_3, 2)
            collision_3[3] = drawRect(rects_3, found_3, colors_3, temp_3, 3)
            collision_3[4] = drawRect(rects_3, found_3, colors_3, temp_3, 4)
            collision_3[5] = drawRect(rects_3, found_3, colors_3, temp_3, 5)
            collision_3[6] = drawRect(rects_3, found_3, colors_3, temp_3, 6)
            collision_3[7] = drawRect(rects_3, found_3, colors_3, temp_3, 7)
            collision_3[8] = drawRect(rects_3, found_3, colors_3, temp_3, 8)
            collision_3[9] = drawRect(rects_3, found_3, colors_3, temp_3, 9)
            collision_3[10] = drawRect(rects_3, found_3, colors_3, temp_3, 10)
            collision_3[11] = drawRect(rects_3, found_3, colors_3, temp_3, 11)

        elif level == 4:
            collision_4[0] = drawRect(rects_4, found_4, colors_4, temp_4, 0)
            collision_4[1] = drawRect(rects_4, found_4, colors_4, temp_4, 1)
            collision_4[2] = drawRect(rects_4, found_4, colors_4, temp_4, 2)
            collision_4[3] = drawRect(rects_4, found_4, colors_4, temp_4, 3)
            collision_4[4] = drawRect(rects_4, found_4, colors_4, temp_4, 4)
            collision_4[5] = drawRect(rects_4, found_4, colors_4, temp_4, 5)
            collision_4[6] = drawRect(rects_4, found_4, colors_4, temp_4, 6)
            collision_4[7] = drawRect(rects_4, found_4, colors_4, temp_4, 7)
            collision_4[8] = drawRect(rects_4, found_4, colors_4, temp_4, 8)
            collision_4[9] = drawRect(rects_4, found_4, colors_4, temp_4, 9)
            collision_4[10] = drawRect(rects_4, found_4, colors_4, temp_4, 10)
            collision_4[11] = drawRect(rects_4, found_4, colors_4, temp_4, 11)
            collision_4[12] = drawRect(rects_4, found_4, colors_4, temp_4, 12)
            collision_4[13] = drawRect(rects_4, found_4, colors_4, temp_4, 13)
            collision_4[14] = drawRect(rects_4, found_4, colors_4, temp_4, 14)
            collision_4[15] = drawRect(rects_4, found_4, colors_4, temp_4, 15)

        elif level == 5:
            collision_5[0] = drawRect(rects_5, found_5, colors_5, temp_5, 0)
            collision_5[1] = drawRect(rects_5, found_5, colors_5, temp_5, 1)
            collision_5[2] = drawRect(rects_5, found_5, colors_5, temp_5, 2)
            collision_5[3] = drawRect(rects_5, found_5, colors_5, temp_5, 3)
            collision_5[4] = drawRect(rects_5, found_5, colors_5, temp_5, 4)
            collision_5[5] = drawRect(rects_5, found_5, colors_5, temp_5, 5)
            collision_5[6] = drawRect(rects_5, found_5, colors_5, temp_5, 6)
            collision_5[7] = drawRect(rects_5, found_5, colors_5, temp_5, 7)
            collision_5[8] = drawRect(rects_5, found_5, colors_5, temp_5, 8)
            collision_5[9] = drawRect(rects_5, found_5, colors_5, temp_5, 9)
            collision_5[10] = drawRect(rects_5, found_5, colors_5, temp_5, 10)
            collision_5[11] = drawRect(rects_5, found_5, colors_5, temp_5, 11)
            collision_5[12] = drawRect(rects_5, found_5, colors_5, temp_5, 12)
            collision_5[13] = drawRect(rects_5, found_5, colors_5, temp_5, 13)
            collision_5[14] = drawRect(rects_5, found_5, colors_5, temp_5, 14)
            collision_5[15] = drawRect(rects_5, found_5, colors_5, temp_5, 15)
            collision_5[16] = drawRect(rects_5, found_5, colors_5, temp_5, 16)
            collision_5[17] = drawRect(rects_5, found_5, colors_5, temp_5, 17)
            collision_5[18] = drawRect(rects_5, found_5, colors_5, temp_5, 18)
            collision_5[19] = drawRect(rects_5, found_5, colors_5, temp_5, 19)
            collision_5[20] = drawRect(rects_5, found_5, colors_5, temp_5, 20)
            collision_5[21] = drawRect(rects_5, found_5, colors_5, temp_5, 21)
            collision_5[22] = drawRect(rects_5, found_5, colors_5, temp_5, 22)
            collision_5[23] = drawRect(rects_5, found_5, colors_5, temp_5, 23)

        # Timer text
        timerText = text_format(str(initialTimer), font, 60, WHITE)

        # Live text
        livesText = text_format('Lives '+str(lives), font, 40, RED)

        # Runs timer 1 per second
        if gameStarts == False:
            if initialTimer != 0:

                screen.blit(timerText, (500, 50))

            else:

                # Game starts
                gameStarts = True
                found_1 = [None, None, None, None]
                found_2 = [None, None, None, None, None, None, None, None]
                found_3 = [None, None, None, None, None, None, None, None,None,None,None,None]
                found_4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
                found_5 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None]

                # Set temporary to None so that there is no more showing of textures
                temp_1 = [None, None, None, None]
                temp_2 = [None, None, None, None, None, None, None, None]
                temp_3 = [None, None, None, None, None, None, None, None, None, None, None, None]
                temp_4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
                temp_5 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None]

        else:
            screen.blit(livesText, (450, 50))   # Display lives

            if initialTimer == 0 and clicked == 2:
                temp_1 = [None, None, None, None]
                temp_2 = [None, None, None, None, None, None, None, None]
                temp_3 = [None, None, None, None, None, None, None, None,None,None,None,None]
                temp_4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
                temp_5 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None]

                clicked = 0

        # After draw, check event

        for event in pygame.event.get():
            if event.type == QUIT:
                gameExit = True

            elif event.type == MOUSEBUTTONDOWN:
                # Only play game if not pause
                if gameStarts == True:
                    if level == 1:
                        #index and value
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
                                                pygame.mixer.music.load(correct)
                                                pygame.mixer.music.play(0)
                                            # Find out if win
                                            totalWins = sum([1 for i in found_1 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_1):
                                               # print('Victory')
                                                level = 2
                                                # Reset all values to start on level 2
                                                temp_2 = [True, True, True, True, True, True, True, True]
                                                lives = 5               # Set lives back to 5
                                                gameStarts = False
                                                initialTimer = 5
                                                continue            # Jump to next iteration
                                            temp_1 = [None, None, None, None]
                                        else:
                                            lives -= 1          # Subtract lives
                                            initialTimer = 1    # Set timer to give time to look at different matches (otherwise is instant)
                                            pygame.mixer.music.load(incorrect)
                                            pygame.mixer.music.play(0)

                    elif level == 2:
                        for i,item in enumerate(collision_2):
                            # Check if mouse click occurred inside item
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_2[i] != True:
                                    clicked += 1  # Always increase counter of clicks if click valid
                                    temp_2[i] = True        # Temporary record which rectangle was clicked
                                    if clicked == 2:
                                        two_clicks = [i for i,v in enumerate(temp_2) if v is not None]
                                        if two_clicks in wins_2:
                                            for i in two_clicks:
                                                found_2[i] = True
                                                pygame.mixer.music.load(correct)
                                                pygame.mixer.music.play(0)
                                            # Find out if win
                                            totalWins = sum([1 for i in found_2 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_2):
                                                #print('Victory')
                                                level = 3
                                                # Reset all values to start on level 3
                                                temp_3 = [True, True, True, True, True, True,True,True,True,True,True,True]
                                                lives = 5  # Set lives back to 5
                                                gameStarts = False
                                                initialTimer = 8
                                                continue            # Jump to next iteration
                                            temp_2 = [None, None, None, None,None,None,None,None]

                                        else:
                                            lives -= 1          # Subtract lives
                                            initialTimer = 1    # Set timer to give time to look at different matches (otherwise is instant)
                                            pygame.mixer.music.load(incorrect)
                                            pygame.mixer.music.play(0)

                    elif level == 3:
                        for i,item in enumerate(collision_3):
                            # Check if mouse click occurred inside item
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_3[i] != True:
                                    clicked += 1  # Always increase counter of clicks if click valid
                                    temp_3[i] = True        # Temporary record which rectangle was clicked
                                    if clicked == 2:
                                        two_clicks = [i for i,v in enumerate(temp_3) if v is not None]
                                        if two_clicks in wins_3:
                                            for i in two_clicks:
                                                found_3[i] = True
                                                pygame.mixer.music.load(correct)
                                                pygame.mixer.music.play(0)
                                            # Find out if win
                                            totalWins = sum([1 for i in found_3 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_3):
                                                #print('Victory')
                                                level = 4
                                                # Reset all values to start on level 4
                                                temp_4 = [True, True, True, True, True, True,True,True,True,True,True,True,True,True,True,True]
                                                lives = 5
                                                gameStarts = False
                                                initialTimer = 10       # Set timer back to 10

                                                continue            # Jump to next iteration
                                            temp_3 = [None, None, None, None,None,None,None,None,None,None,None,None]

                                        else:
                                            lives -= 1          # Subtract lives
                                            initialTimer = 1    # Set timer to give time to look at different matches (otherwise is instant)
                                            pygame.mixer.music.load(incorrect)
                                            pygame.mixer.music.play(0)

                    elif level == 4:
                        for i,item in enumerate(collision_4):
                            # Check if mouse click occurred inside item
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_4[i] != True:
                                    clicked += 1  # Always increase counter of clicks if click valid
                                    temp_4[i] = True        # Temporary record which rectangle was clicked
                                    if clicked == 2:
                                        two_clicks = [i for i,v in enumerate(temp_4) if v is not None]
                                        if two_clicks in wins_4:
                                            for i in two_clicks:
                                                found_4[i] = True
                                                pygame.mixer.music.load(correct)
                                                pygame.mixer.music.play(0)
                                            # Find out if win
                                            totalWins = sum([1 for i in found_4 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_4):
                                               # print('Victory')
                                                level = 5
                                                # Reset all values to start on level 4
                                                temp_5 = [True, True, True, True, True, True,True,True,True,True,True,True,True,True,True,True, True, True, True, True, True, True, True, True]
                                                lives = 5
                                                gameStarts = False
                                                initialTimer = 14      # Set timer back to 14
                                                continue            # Jump to next iteration
                                            temp_4 = [None, None, None, None,None,None,None,None,None,None,None,None, None, None, None, None]

                                        else:

                                            lives -= 1          # Subtract lives
                                            initialTimer = 1    # Set timer to give time to look at different matches (otherwise is instant)
                                            pygame.mixer.music.load(incorrect)
                                            pygame.mixer.music.play(0)

                    elif level == 5:
                        for i,item in enumerate(collision_5):
                            if item.collidepoint(event.pos):
                                # If item was not clicked already
                                if found_5[i] != True:
                                    clicked += 1  # Always increase counter of clicks if click valid
                                    temp_5[i] = True  # Temporary record which rectangle was clicked
                                    if clicked == 2:
                                        two_clicks = [i for i, v in enumerate(temp_5) if v is not None]
                                        if two_clicks in wins_5:
                                            for i in two_clicks:
                                                found_5[i] = True
                                                pygame.mixer.music.load(correct)
                                                pygame.mixer.music.play(0)

                                            # Find out if win
                                            totalWins = sum([1 for i in found_5 if i is not None])
                                            # Compare total wins to length of possible total wins
                                            if totalWins == len(found_5):
                                                count = 1
                                                #print('Victory')
                                            temp_5 = [None, None, None, None,None,None,None,None,None,None,None,None, None, None, None, None,None,None,None,None, None, None, None, None]
                                        else:
                                            lives -= 1
                                            initialTimer = 1  # Set timer to give time to look at different matches (otherwise is instant)
                                            pygame.mixer.music.load(incorrect)
                                            pygame.mixer.music.play(0)



        # Reduce timer only if game has not start
        if currentTicks == 0:
            if initialTimer > 0:
                initialTimer -= 1  # Count down

        if currentTicks == FPS:
            currentTicks = 0  # Counts ticks once per second
        else:
            currentTicks += 1  # Increase ticks if mark not at FPS (that is if number is not 30)

        if count == 1:
            screen.fill(BLACK)
            CText = text_format('YOU WIN!', font, 80, GREEN_YELLOW)
            screen.blit(CText,(305,90))
            pygame.display.flip()
            pygame.display.update()

        else:
            pygame.display.update()


        if lives == 0:
            screen.fill(BLACK)
            GText = text_format('GAMEOVER.',font,80,RED)
            screen.blit(GText,(280,90))
            pygame.display.flip()
            pygame.display.update()


        else:
            pygame.display.update()

        clock.tick(FPS)

#Initialize the Game
main_menu()
#pygame.quit()

#quit()
