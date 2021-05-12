#! usr/bin/env python3
import hurrican_data as data

def hurrican_scale(speed):
    prefix = "\nThe category of the hurrican is "
    
    if speed<74:
        print("\nIt is not a hurrican.")
    
    elif 74<speed<95:
        print(prefix+"ONE.")
        data.print_damage("ONE")
    
    elif 96<speed<110:
        print(prefix+"TWO.")
        data.print_damage("TWO")

    elif 111<speed<129:
        print(prefix+"THREE.")
        data.print_damage("THREE")

    elif 130<speed<156:
        print(prefix+"FOUR.")
        data.print_damage("FOUR")

    else:
        print(prefix+"FIVE.")
        data.print_damage("FIVE")

while True:
    try:
        usr_input = input("What is the speed of the wind in mph?\n>")
        speed = int(usr_input)

        hurrican_scale(speed)
        break
    except ValueError:
        print("Please input a valid number.\n")
