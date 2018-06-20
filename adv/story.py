from __future__ import (nested_scopes, generators, division, absolute_import,
with_statement, print_function, unicode_literals)
# import pickle

# from adventurelib import *
from adventurelib import Room, Item, say, when, Bag, start, set_context, get_context

# initialize rooms
Room.items = Bag()
Room.gold = 0

#locations
Width = 9
Height = 7
Room_List = []
for x in range(0,Width):
    Room_List.append([Room("") for y in range(0,Height)])


current_room = starting_room = Room_List[3][0] = Room("""
you awaken in a dungeon cellar. in front of you lies a notebook which reads, 
Take me with you to find the letters. only one phrase will set you free
""")

Room_List[3][1] = Room_List[3][0].north = Room("""
you proceed toward the next room. this room is dimly lit and smells of mold.
""")

Room_List[3][2] = Room_List[3][1].north = Room("""
You press on through, coming to a room with a single candle and table.
""")

Room_List[3][3] = Room_List[3][2].north = Room("""
""")

Room_List[3][4] = Room_List[3][3].north = Room("""
""")

Room_List[3][5] = Room_List[3][4].north = Room("""
""")

Room_List[3][6] = Room_List[3][5].north = Room("""
""")

Room_List[4][3] = Room_List[3][3].east = Room("""
""")

Room_List[5][3] = Room_List[4][3].east = Room("""
""")

Room_List[6][3] = Room_List[5][3].east = Room("""
""")

Room_List[6][4] = Room_List[6][3].north = Room("""
""")

Room_List[6][5] = Room_List[6][4].north = Room("""
""")

Room_List[6][6] = Room_List[6][5].north = Room("""
""")

Room_List[6][2] = Room_List[6][3].south = Room("""
""")

Room_List[6][1] = Room_List[6][2].south = Room("""
""")

Room_List[6][0] = Room_List[6][1].south = Room("""
""")

Room_List[2][3] = Room_List[3][3].west = Room("""
""")

Room_List[1][3] = Room_List[2][3].west = Room("""
""")

Room_List[0][3] = Room_List[1][3].west = Room("""
""")

Room_List[0][4] = Room_List[0][3].north = Room("""
""")

Room_List[0][5] = Room_List[0][4].north = Room("""
""")

Room_List[0][6] = Room_List[0][5].north = Room("""
""")

Room_List[0][2] = Room_List[0][3].south = Room("""
""")

Room_List[0][1] = Room_List[0][2].south = Room("""
""")

Room_List[0][0] = Room_List[0][1].south = Room("""
""")



Room_R1 = Room("""
you head right and enter the servants quarters
""")

Room_3  = Room_R1.west = Room("""
You are in a cranky wizard chambers.
""")


Room_L1 = Room_3.west = Room("""
You are in a spacious tower.
""")


# letter_bank is an array of item letters.
# they will be added to the notebook
letter_bank = []
for letter in "THANKS FOR PLAYING":
    letter_bank.append(Item(letter))

# item creation
Item.amount = 0
mallet = Item('rusty mallet', 'mallet')
spoon = Item('greasy spoon', 'spoon')

wand = Item('wand')

compass = Item('Compass')

ball = Item('Crystal ball', 'ball')

# location properties and items
Room_List[3][1].items = Bag({compass})
Room_List[3][1].gold = 5

Room_List[3][2 ].gold = 6

#wizard_chamber.items = Bag({wand})

#tower.items = Bag({ball, letter_bank[0]})


# make the notebook to store letters
class Notebook(Item):
    letters_found = Bag()


notebook = Notebook('Notebook', 'book', 'notes')

# initialize the players inventory
inventory = Bag()
inventory.gold = 0
inventory.add(notebook)

# action functions
@when('north', direction='north')
@when('n', direction='north')
@when('south', direction='south')
@when('s', direction='south')
@when('east', direction='east')
@when('e', direction='east')
@when('west', direction='west')
@when('w', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
        if room == Room_L1: #magic_forest:
            set_context('magic_aura')
        else:
            set_context('default')
    else:
        say("You can't currently go %s." % direction)
        look()


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        if obj in letter_bank:
    #        print("this is a letter")
            nb = inventory.find("notebook")
            if nb:
                nb.letters_found.add(obj)
            else:
                say("But you do not have a way to record it, so you put it back down on the ground.")
                current_room.items.add(obj)
        else:
            inventory.add(obj)
    elif item == 'gold':
        inventory.gold += current_room.gold
        say('You pick up the {} gold'.format(current_room.gold))
        current_room.gold = 0
    else:
        say('There is no %s here.' % item)

@when('use ITEM')
def use(item):
    current_item = inventory.find(item)
    if not current_item:
        say("you do not have that item")
    elif current_item is compass:
        say(current_room.exits())
    elif current_item is ball:
        for dir in current_room.exits():
            say(" You gaze into the crystal and picture yourself moving {}.:".format(dir))
            say(current_room.exit(dir))
    else:
        say("Oak's words echoed... There's a time and place for everything, but not now.")
      #say("There is currently no use for {} here".format(current_item))
# add ability to drop gold
@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

@when('l')
@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            if i.amount > 0:
                say('There are {} {} here.'.format(i.amount,i))
            else:
                say('A %s is here.' % i)
    if current_room.gold > 0:
        say("There is {} gold on the ground".format(current_room.gold))

@when('i')
@when('inv')
@when('inventory')
def show_inventory():
    single = True
    say('You have: ')
    for thing in inventory:
        if thing.amount > 0:
            say("{} {}".format(thing.amount,thing))
            single = False
        else:
            if single:
                say(thing)
                single = False
            else:
                say(", "+str(thing))
    if inventory.gold > 0:
        if not single:
            say(",")
        say("{} gold".format(inventory.gold))
        single = False
    nb = inventory.find("Notebook")
    if nb and nb.letters_found:
        say("You have found the following letters: ")
        for letter in nb.letters_found:
            say(letter)
@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura', magic=None)
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    else:
        say("You cast " + magic)


#save and load not currently working
# @when('save')
#def save():
#    data = {"current_room": current_room, "inventory": inventory}
#    #pickle.dump(data, open("save.p", "wb"))
#    say("Game saved. ")


# @when('load')
#def load():
#   # data = pickle.load(open("save.p", "rb"))
##    global current_room
#    current_room = data["current_room"]
#    global inventory
#    inventory = data["inventory"]
#    say("Game loaded. ")
#    look()
#    show_inventory()

if __name__ == "__main__":
    look()
    start()

