# Game TIC TAC TOE:
import math
import random

# Hellow User:
from functions import *

running = True
game_done = False
player1 = "X"
player2 = "O"
icon_slected = "X"


if table_matrix != "1":
    table = [["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ]]
else:
    table = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]


hello()

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
                break
        if icon_slected == player1:                                             ## Switch the icon for the next turn
            icon_slected = player2
        else:
            icon_slected = player1
    else:
        print("Invalid input. Please choose a row and column within the valid range.")
    if game_done:
        running = False
        game_done = True
        break
print("Game Done!")
