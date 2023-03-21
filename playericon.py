def player_icon(icon):
    print("Chose your player icon : (X) or (O)")
    if icon == "1":
        print("icon selected is : X ")
    elif icon == "2":
        print("icon selected is : O ")
    else:
        print("Invalid input. Please select 1 or 2 ")   
icon_slected = input("Select your player icon :\n(1): X\n(2): O\n> ")
icon_slected = icon_slected.capitalize()
player_icon(icon=icon_slected)