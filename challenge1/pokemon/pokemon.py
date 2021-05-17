#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    choice = input("What is the pokemon you like?\n>")
    url = f"https://pokeapi.co/api/v2/pokemon/{choice}"
    pokeapi = requests.get(url).json()
    img = pokeapi["sprites"]["front_default"]
    print(img)
    
    r = requests.get(img)
    open(f"/home/student/static/{choice}.jpg","wb").write(r.content)
    print(f"The number of game indices is {len(pokeapi['game_indices'])}")
    
    print("Moves:")
    for move in pokeapi['moves']:
        print(f"{move['move']['name']}",end=" ")



main()
  
