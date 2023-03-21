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
icon_slected = icon_slected.capitalize()
player_icon(icon=icon_slected)