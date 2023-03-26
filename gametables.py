def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
    elif table == "2":
        print("Board selected - 4X4 board.")        
    elif table == "3":
        print("Game Shutdown.")
        quit("Error 1")
    else:
        print("Invalid input. Please select 1 or 2 or 3")   

table_matrix = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")
game_tables(table_matrix)