# # Game TIC TAC TOE:
import math
import functions
print("Hello user this is tha main menu for Tic-Tac-Toe game chose of the options : ")

# Game Settings
from functions import game_settings # this function set the game menu to stdout

# Player Icon: "X" or "O"
from playericon import icon_slected # plyer icon like "X" or "O"

# from tables import table_graphics # this function set the size of the table "3X3" or "4X4"
# from tables import table_size

import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.random.random((50,50)))
plt.colorbar()
plt.show()