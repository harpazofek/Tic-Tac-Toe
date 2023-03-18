table_size = ""
def game_tables(table):
    if table == "1":
        print("Board selected - 3X3 board.")
    elif table == "2":
        print("Board selected - 4X4 board.")
    else:
        print("Invalid input. Please select 1 or 2 or Quit")   
table_size = input("Which board do you prefer to play on?\n(1) 3X3\n(2) 4X4\n(Quit) \n> ")
table_size = table_size.lower()

from main import table_size
if table_size == 1:
    print("Test")
else:
    print(((f
["_", "_", "_" ], ["_", "_", "_" ], ["_", "_", "_" ]

        )))
