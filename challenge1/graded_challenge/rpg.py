#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
class Police:
    def __init__(self,inventory):
        self.hp = 100
        self.inventory = inventory
    def is_dead(self):
        return self.hp<=0

    def attack(self,weapon,terrorist):
        if weapon == 'm16':
            terrorist.hp -= 30
        if weapon == 'flashbang':
            terroris.status = 'frozen'
        if weapon == 'grenade':
            terrorist.hp -= 50
            self.hp -= 25
    def negotiate(terrorist):
        if terrorist.hp<100:
            print('negotiation failed')
        if random.randint(1,3)==2:    
            terrorist.status = "persuaded"

class Terrorist:
    def __init__(self,status):
        self.hp = 100
        self.inventory = ['ak47']
        self.status = 'insane'
    def attack(self,police):
        police.hp -=40
        self.status = 'insane'
    



def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ', currentRoom)
  #print the current inventory
  print('Inventory : ', str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a '+ display_item(rooms[currentRoom]['item']))
  print("---------------------------")

def display_item(items):
    str =""
    for item in items:
        str += item+' '
    return str

#combat mode
def combat():
    



#an inventory, which is initially empty
inventory = ['knife']   

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            'Outside':{
                  'inside': 'Hall',
                  'item' : ['m16','flashbang','grenade']
                },
            'Hall' : {
                  'outside'  : 'Outside',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : ['terrorist','hostages'],
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'health pack',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item'  : ['health pack'],
            }

#start the player in the Hall
currentRoom = 'Outside'

showInstructions()

#loop forever
while True:

  showStatus()

  #if you are in the kitchen, the enter combat mode
  if currentRoom == 'Kitchen':
      combat()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')


  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      rooms[currentRoom]['item'].remove(move[1])
      if len(rooms[currentRoom]['item'])==0:
          del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  """     
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
 """
