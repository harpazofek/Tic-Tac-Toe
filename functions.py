def game_settings(lobby):
    if lobby == "1":
        print("Board selected - 3X3 board.")
    elif lobby == "2":
        print("Board selected - 4X4 board.")
    elif lobby == "quit":
        print("Game Shotdown.")
    else:
        print("Invalid input. Please select 1 or 2 or Quit")   
board_size = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(Quit) \n> ")
board_size = board_size.lower()

game_settings(lobby=board_size)