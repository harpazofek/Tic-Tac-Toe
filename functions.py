## This fuction print hello to the stdout
def hello():
    print("Hello user this is tha main menu for Tic-Tac-Toe game chose of the options : ")


## With this function we can select the icon of the player.
def get_icon():
    icon_selected = input("Select your player icon:\n(1) X\n(2) O\n> ")
    if icon_selected == "1":
        return "X"
    elif icon_selected == "2":
        return "O"
    else:
        print("Invalid input. Please select 1 or 2.")
        return get_icon()



## With this function we can select board table of the game
def game_tables():
    table_matrix = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n> ")
    if table_matrix == "1":
        print("Board selected - 3X3 board.")
        table = [["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]]
        return table
    elif table_matrix == "2":
        print("Board selected - 4X4 board.")
        table = [["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ], ["_", "_", "_", "_" ]]
        return table
    else:
        print("Invalid input. Please select 1 or 2 ")
    return None
    


## This functions will print the board table like a board and not like list
## Its deppend of the board selection if you select the 3X3 or the 4X4 
def displayboard(table):
    print(len(table))
    if len(table) != 4:
        for row in table:                   
            print("+---+---+---+")
            print("|", end="")
            for col in row:
                print(" {} |".format(col), end="")
            print()
        print("+---+---+---+")
    elif len(table) != 3:
        for row in table:                                                               
            print("+---+---+---+---+")
            print("|", end="")
            for col in row:
                print(" {} |".format(col), end="")
            print()
        print("+---+---+---+---+")
    else:
        print("Display board")
        quit()



## With this function I going to check if one of the player win the game by row/colum/slant
def checkTable(table, player):
    size = len(table)
    if size != 4:
        for win_row in table:
            if win_row.count(player) >= size:
                return player
        for win_col in table:
            if table[0][0] == table[1][0] == table[2][0] == (f'{player}'):
                return player
            elif table[0][1] == table[1][1] == table[2][1] == (f'{player}'):
                return player
            elif table[0][2] == table[1][2] == table[2][2] == (f'{player}'):
                return player
        for slant_win in table:
            if table[0][0] == table[1][1] == table[2][2] == (f'{player}'):
                return player
            elif table[0][2] == table[1][1] == table[2][0] == (f'{player}'):
                return player
    else:
        for win_row in table:
            if win_row.count(player) >= size:
                return player
        for win_col in table:
            if table[0][0] == table[1][0] == table[2][0] == table[3][0] == (f'{player}'):
                return player
            elif table[0][1] == table[1][1] == table[2][1] == table[3][1] == (f'{player}'):
                return player
            elif table[0][2] == table[1][2] == table[2][2] == table[3][2] == (f'{player}'):
                return player
        for slant_win in table:
            if table[0][0] == table[1][1] == table[2][2] == table[3][3] == (f'{player}'):
                return player
            elif table[0][2] == table[1][1] == table[2][0] == table[3][0] == (f'{player}'):
                return player
    return None


