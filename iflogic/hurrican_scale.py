#! usr/bin/env python3

def hurrican_scale(speed):
    prefix = "\nThe category of the hurrican is "
    if speed<74:
        print("\nIt is not a hurrican.")
    elif 74<speed<95:
        print(prefix+"ONE.")
    elif 96<speed<110:
        print(prefix+"TWO.")
    elif 111<speed<129:
        print(prefix+"THREE.")
    elif 130<speed<156:
        print(prefix+"FOUR.")
    else:
        print(prefix+"FIVE.")

while True:
    try:
        usr_input = input("What is the speed of the wind in mph?\n>")
        speed = int(usr_input)

        hurrican_scale(speed)
        break
    except ValueError:
        print("Please input a valid number.\n")
