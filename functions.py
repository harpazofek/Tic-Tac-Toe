def hello():
    print("Hello user this is tha main menu for Tic-Tac-Toe game chose of the options : ")



def player_icon(icon):
    if icon == "1":
        icon = "X"
        print("icon selected is : X ")
    elif icon == "2":
        icon == "O"
        print("icon selected is : O ")
    else:
        print("Invalid input. Please select 1 or 2 ")   
    icon_slected = input("Select your player icon :\n(1): X\n(2): O\n> ")
    icon_slected = icon_slected.upper()



def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
    elif table == "2":
        print("Board selected - 4X4 board.")        
    elif table == "3":
        quit("Error 1 Game Shutdown.")
    else:
        print("Invalid input. Please select 1 or 2 or 3")   
table_matrix = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")

def displayboard(table):
    for row in table:                                                               ## This for loop was present the table like table and not like the list
        print("+---+---+---+")
        print("|", end="")
        for col in row:
            print(" {} |".format(col), end="")
        print()
    print("+---+---+---+") 


def checkTable(table, player):
    size = len(table)
    for win in table:
        if win.count(player) >= size:
            return player
    # for i in range(size):
    #     for j in range(size):
    #         if  table[i][j*size]: col1 +=1 
    #         col2 = table[i][j*size + 1] 
    #         col2 = table[i][j*size + 2] 
    # if col1 == size    
    return None





