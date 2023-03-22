
# Game TIC TAC TOE:
import math

# Hellow User:
from hellow_user import hello

# Game Settings
# from appmenu import game_settings # this function set the game menu to stdout
# print(game_settings)

# This function select the table size like "3X3 4X4 etc..."
# from gametables import table_size

# Player Icon: "X" or "O"
from playericon import icon_slected # plyer icon like "X" or "O"
# print(f'{icon_slected} for debug')





def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
    elif table == "2":
        print("Board selected - 4X4 board.")        
    elif table == "3":
        print("Game Shotdown.")
        for quit in table:
            break
    else:
        print("Invalid input. Please select 1 or 2 or 3")   
table_matrix = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")
game_tables(table_matrix)


running = True
game_done = False
output = ""


while running:
        if icon_slected != 2:
            icon_slected = "X"
        else:
             icon_slected = "O"
        if table_matrix != 2:
            table_size = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
        elif table_matrix != 1:
            table_size = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
        else:
            table_size = 3
            print("Game PowerOff")
            break
        rowlst = int(input("Row selection :  "))
        collst = int(input("Colum selection : "))
        if rowlst != int or collst != int:
            running = False
            # raise Exception('invalid input!')
        elif rowlst and collst == int:
            print(table_size)
        else:
             print("Try to play again and chose a number in colum and rom like 1-9")
        print(table_size)
        for row in table_size:
                print("+---+---+---+")
                print("|", end="")
                for col in row:
                    print(" {} |".format(col), end="")
                print()
        print("+---+---+---+")

        
         
print("Game Done!")
game_done = True
print("GG - ba lan ;) ")