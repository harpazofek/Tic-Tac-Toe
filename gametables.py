def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
        print([f"1", "2", "3" ], [f"4", "5", "6" ], [f"7", "8", "9" ])
    elif table == "2":
        print("Board selected - 4X4 board.")
        print(["1", "2", "3" ], ["4", "5", "6" ], ["7", "8", "9" ])
    elif table == "3":
        print("Game Shotdown.")
        
    else:
        print("Invalid input. Please select 1 or 2 or Quit")   
table_size = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")
table_size = table_size.lower()
game_tables(table=table_size)

# if table == 1:
#     print(["1", "2", "3" ], ["4", "5", "6" ], ["7", "8", "9" ])
# elif table_size == 2:
#     print(["1", "2", "3" ], ["4", "5", "6" ], ["7", "8", "9" ], ["10", "11", "12" ])
# else:
#     print('Table was not fund')