# Game TIC TAC TOE: #
import math
import random

# Hellow User:
from functions import *

hello()
icon_slected = get_icon()
play_again = True
table = game_tables()
while play_again:
    running = True
    player1 = "X"
    player2 = "O"
    x = 0
    while table == None:
        x += 1
        if x > 2:
            play_again = False 
            break
    if not play_again: break
    turn = 16 if len(table) != 3 else 9

    while running:          
        displayboard(table)
        rowlst = int(input(f'Turn {icon_slected} Row selection: '))
        collst = int(input(f'Turn {icon_slected} Column selection: '))

        if 1 <= rowlst <= len(table) and 1 <= collst <= len(table[0]):      ## Check if the row and column are within the valid range
            if table[rowlst-1][collst-1] != "_":                            ## Check if the cell is already select
                print("That cell is already occupied.")
            else:
                table[rowlst-1][collst-1] = icon_slected
                if checkTable(table, icon_slected) != None:
                    print(f'Player {icon_slected} win!!!!')
                    displayboard(table)
                    running = False
            if icon_slected == player1:                                             ## Switch the icon for the next turn
                icon_slected = player2
            else:
                icon_slected = player1
        else:
            print("Invalid input. Please choose a row and column within the valid range.")
        turn -= 1
        if turn == 0:
            print("Draw!")
            displayboard(table)
            running = False
    print("Game Over!")
    
    ## Reseting the table and the game
    if input("Do you want to play agin? : y/n ").upper() != 'Y':
        break
    else:
        table = game_tables()           
        running = True
        



