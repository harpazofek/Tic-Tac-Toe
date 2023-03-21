
# Game TIC TAC TOE:
import math

# Hellow User:
from hellow_user import hello

# Game Settings
# from appmenu import game_settings # this function set the game menu to stdout
# print(game_settings)

# This function select the table size like "3X3 4X4 etc..."
from gametables import table_size
table_size = ""
if table_size == "3":
    raise SystemExit
# if table_size == "3":
#     raise Exception("Quit Game")
# Player Icon: "X" or "O"
from playericon import icon_slected # plyer icon like "X" or "O"
# print(f'{icon_slected} for debug')

running = True
game_done = False
table = {table_size}
icon = icon_slected

while running:
        print(f'Player icon turn is : {icon_slected}')
        print(f'{table_size}')
        print
        row_selection = int[input("Row selection :  ")]
        colum_selection = int[input("Colum selection : ")]
        if row_selection or colum_selection == str:
            running = False
        elif row_selection and colum_selection == int:
            print(f'{row_selection}, {colum_selection}')
        else: 
            print("Game Done!")
            game_done = True
print("GG - ba lan ;) ")