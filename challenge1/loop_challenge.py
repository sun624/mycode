#!usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Function 1
def function1(index):
    print("\nThis is Function1")
    print(f"Animals/plants in {farms[index]['name']}:")
    for animal in farms[index]["agriculture"]:
        print(animal)

# Function2
def function2():
    print("\nThis is Function2")
    usr_input = input("Please choose a farm\n1. NE farm\n2. W farm\n3. SE farm\n>")
    function1(int(usr_input)-1)



# Function3
def function3(farms):
    print("\nThis is Function3")
    plants = ["carrots","celery"]
    usr_input = input("Please choose a farm\n1. NE farm\n2. W farm\n3. SE farm\n>")
    for animal in farms[int(usr_input)-1]["agriculture"]:
        if animal not in plants:
            print(animal)



function1(0)
function2()
function3(farms)


