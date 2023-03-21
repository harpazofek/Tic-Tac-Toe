
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
        table_size = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
        for row in table_size:
                print("+---+---+---+")
                print("|", end="")
                for col in row:
                    print(" {} |".format(col), end="")
                print()
        print("+---+---+---+")
    elif table == "2":
        print("Board selected - 4X4 board.")        
        table_size = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
        for row in table_size:
                print("+---+---+---+")
                print("|", end="")
                for col in row:
                    print(" {} |".format(col), end="")
                print()
        print("+---+---+---+")
    elif table == "3":
        print("Game Shotdown.")
        for quit in table:
            break
    else:
        print("Invalid input. Please select 1 or 2 or 3")   
table_matrix = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")
game_tables(table=table_matrix)


running = True
game_done = False


while running:
        print(f'Player icon turn is : {icon_slected}')
        print(f'{table_matrix}')
        print
        row = input("Row selection :  ")
        colum = input("Colum selection : ")
        if row or colum == str:
            running = False
        elif row and colum == int:
            table_matrix[{row}, {colum}]
        else: 
            print("Game Done!")
            game_done = True
print("GG - ba lan ;) ")