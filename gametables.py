
# # mosh
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in matrix:
#         print(item)


def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
        table = [
        ["_", "_", "_" ], 
        ["_", "_", "_" ], 
        ["_", "_", "_" ], 
        ]
        # table[0][1] = 20
        print(table)
    elif table == "2":
        print("Board selected - 4X4 board.")
        table = [
        ["_", "_", "_" ], 
        ["_", "_", "_" ], 
        ["_", "_", "_" ], 
        ["_", "_", "_" ]
        ]
        # table[1][2] = 40
        # print(table[1][2])
        print(table)
    elif table == "3":
        print("Game Shotdown.")
        return
    else:
        print("Invalid input. Please select 1 or 2 or 3")   
table_size = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(3) Quit \n> ")
table_size = table_size.lower()
game_tables(table=table_size)

