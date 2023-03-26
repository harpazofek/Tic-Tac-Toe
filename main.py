
# Game TIC TAC TOE:
import math
import random

# Hellow User:
from hellow_user import hello

# Settings

# Player Icon: "X" or "O"
from playericon import icon_slected
# print(f'{icon_slected} for debug')

# This function select the table size like "3X3 4X4 etc..."
from gametables import table_matrix

running = True
game_done = False
player1 = "X"
player2 = "O"
# icon_slected = "X"
# empty_list = []
# pcplayer = True

if table_matrix != "1":
    table = [["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ]]
else:
    table = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
if icon_slected != "1":
    icon_slected = "O"
else:
    icon_slected = "X"
while running:
    for row in table:                                                               ## This for loop was present the table like table and not like the list
        print("+---+---+---+")
        print("|", end="")
        for col in row:
            print(" {} |".format(col), end="")
        print()
    print("+---+---+---+")            
    rowlst = int(input("Row selection: "))
    collst = int(input("Column selection: "))
    if 1 <= rowlst <= len(table) and 1 <= collst <= len(table[0]):      ## Check if the row and column are within the valid range
        if table[rowlst-1][collst-1] != "_":                            ## Check if the cell is already select
            print("That cell is already occupied.")
        else:
            table[rowlst-1][collst-1] = icon_slected
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
