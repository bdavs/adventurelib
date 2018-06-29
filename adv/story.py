from __future__ import (nested_scopes, generators, division, absolute_import,
                        with_statement, print_function, unicode_literals)
# import pickle

# from adventurelib import *
from adventurelib import Room, Item, say, when, Bag, start, set_context
# , get_context
import mechanics

# initialize rooms
Room.items = Bag()
Room.gold = 0
Room.visited = 0

# locations
Width = 7
Height = 7
Room_List = []
for x in range(0, Width):
    Room_List.append([Room("") for y in range(0, Height)])


current_room = starting_room = Room_List[3][0] = Room("""
You awaken in a dungeon cellar. in front of you lies a notebook which reads,
Take me with you to find the letters. only one phrase will set you free
""")
starting_room.visited = 1

Room_List[3][1] = Room_List[3][0].north = Room("""
You enter a dimly lit room which smells of elderberries.
""")

Room_List[3][2] = Room_List[3][1].north = Room("""
You enter a brighter room with a desk at its center and one chair.
""")

Room_List[3][3] = Room_List[3][2].north = Room("""
You enter a lavish circular chamber.
""")

Room_List[3][4] = Room_List[3][3].north = Room("""
You enter a room brimmed full of weapons and a sign that reads armory.
""")

Room_List[3][5] = Room_List[3][4].north = Room("""
You enter the room and are immediately assaulted... by the smell of dried meats
""")

Room_List[3][6] = Room_List[3][5].north = Room("""
You enter a room filled with tables and benches. must be the mess
""")

Room_List[4][3] = Room_List[3][3].east = Room("""
You enter what seems to be the servants quarters
""")

Room_List[5][3] = Room_List[4][3].east = Room("""
You enter a room with cots and chests. The beds are made quite nicely.
""")

Room_List[6][3] = Room_List[5][3].east = Room("""
You enter a room with what appears to practice dummies. Some of them look pretty roughed up. Poor bastards
""")

Room_List[6][4] = Room_List[6][3].north = Room("""
You enter a room and regret it. Buckets in the corner ,and the burning of your nose hair, tell you it the lavatory
""")

Room_List[6][5] = Room_List[6][4].north = Room("""
You enter a room lined with mold along the walls
""")

Room_List[6][6] = Room_List[6][5].north = Room("""
You enter a room with a golden throne at its center. Must be the throne room
""")

Room_List[6][2] = Room_List[6][3].south = Room("""
You enter a room with absolutely nothing in it
""")

Room_List[6][1] = Room_List[6][2].south = Room("""
You enter a room adorned with magic symbols. 
""")

Room_List[6][0] = Room_List[6][1].south = door_room = Room(""" 
You enter a room with 16 square indents lining the wall. suddenly you hear 'Reveal what you have found and speak your
answer'
""")

Room_List[2][3] = Room_List[3][3].west = Room("""
You enter a room and find books upon books, to bad you don't know how to read.
""")

Room_List[1][3] = Room_List[2][3].west = Room("""
you enter a room with gadgets and gizmos aplenty
""")

Room_List[0][3] = Room_List[1][3].west = Room("""
You enter a room with chains upon the wall
""")

Room_List[0][4] = Room_List[0][3].north = Room("""
You enter a room with kegs stacked three high. Come back later and lets party.
""")

Room_List[0][5] = Room_List[0][4].north = Room("""
You enter a room with farming tools hanging on the wall, and bags of rotten grain at your feet
""")

Room_List[0][6] = Room_List[0][5].north = Room("""
You enter a room and smell putrid flesh. You see the zombies bumping into walls. don't worry they can't hurt you... yet
""")

Room_List[0][2] = Room_List[0][3].south = Room("""
You enter a room with a giant ring protruding from the wall.
""")

Room_List[0][1] = Room_List[0][2].south = Room("""
You enter a room with all sorts of wares hanging from the wall. 
""")

Room_List[0][0] = Room_List[0][1].south = shop_room = Room("""
You enter the room and see a plump shop keep behind a counter. In an unusually high pitched voice he says 'Welcome to 
Walls Mart, get your crap and get out'
""")

grue_room = starting_room.down = Room("""
You are at the bottom of the ladder. It is pitch black. You have nothing to create light. You are likely to be eaten by a grue
""")

# letter_bank is an array of item letters.
# they will be added to the notebook
letter_bank = []
for letter in "THANKSFORPLAYING":
    letter_bank.append(Item(letter))

# item creation
Item.amount = 0
Item.cost = 0
mallet = Item('rusty mallet', 'mallet')
spoon = Item('greasy spoon', 'spoon')

wand = Item('wand')

compass = Item('Compass')
map = Item('Map')

ball = Item('Crystal ball', 'ball')
ball.cost = 3


# location properties and items
Room_List[3][1].items = Bag({compass})
Room_List[3][1].gold = 5

Room_List[3][2].gold = 6

shop_room.items = Bag({wand})
shop_room.store_items = Bag({ball})
# wizard_chamber.items = Bag({wand})

# tower.items = Bag({ball, letter_bank[0]})


# make the notebook to store letters
class Notebook(Item):
    letters_found = Bag()


notebook = Notebook('Notebook', 'book', 'notes')

# initialize the players inventory
inventory = Bag()
inventory.gold = 0
inventory.add(notebook)

master_item_list = Bag({mallet,spoon,wand,compass,map,ball,notebook,})
for letter in letter_bank:
    master_item_list.add(letter)
    
set_context('starting_room')
    
# action functions
@when('north', direction='north')
@when('n', direction='north')
@when('south', direction='south')
@when('s', direction='south')
@when('east', direction='east')
@when('e', direction='east')
@when('west', direction='west')
@when('w', direction='west')
@when('down', direction='down',context='starting_room')
@when('d', direction='down',context='starting_room')
@when('up', direction='up',context='grue_room')
@when('u', direction='up',context='grue_room')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        current_room.visited = 1
        say('You go %s.' % direction)
        look()
        if room == door_room:
            set_context('final_door')
        elif room == shop_room:
            set_context('shop')
        elif room == starting_room:
            set_context('starting_room')
        elif room == grue_room:
            set_context('grue_room')
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
#           print("this is a letter")
            nb = inventory.find("notebook")
            if nb:
                nb.letters_found.add(obj)
            else:
                say("But you do not have a way to record it, so you put it back down on the ground.")
                current_room.items.add(obj)
        else:
            inventory.add(obj)
    elif item == 'gold':
        if current_room.gold > 0:
            inventory.gold += current_room.gold
            say('You pick up the {} gold'.format(current_room.gold))
            current_room.gold = 0
        else:
            say("There is no gold on the ground here")
    elif current_room == shop_room:
        obj = current_room.store_items.find(item)
        if obj:
            say("You gunna pay for that {}, kid? It costs {} gold. ".format(obj, obj.cost))
        else:
            say('There is no {} on the ground.'.format(item))
    else:
        say('There is no {} on the ground.'.format(item))


@when('use ITEM')
def use(item):
    current_item = inventory.find(item)
    if not current_item:
        say("you do not have that item")
    elif current_item is compass:
        exits = current_room.exits()
        for x in exits:
            say(x)
            next_room = current_room.exit(x)
            if next_room.visited == 0:
                next_room.visited = 3
#        say(current_room.exits())
    elif current_item is ball:
        for dir in current_room.exits():
            say(" You gaze into the crystal and picture yourself moving {}: ".format(dir))
            say(current_room.exit(dir))
    else:
        say("Oak's words echoed... There's a time and place for everything, but not now.")
# say("There is currently no use for {} here".format(current_item))


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
                say('There are {} {} here.'.format(i.amount, i))
            else:
                say('A %s is here.' % i)
    if current_room.gold > 0:
        say("There is {} gold on the ground".format(current_room.gold))
    if current_room == shop_room:
        for i in current_room.store_items:
             say('The {} costs {}'.format(i, i.cost))

@when('i')
@when('inv')
@when('inventory')
def show_inventory():
    single = True
    say('You have: ')
    for thing in inventory:
        if thing.amount > 0:
            say("{} {}".format(thing.amount, thing))
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
    if magic is None:
        say("Which magic you would like to spell?")
    else:
        say("You cast " + magic)


# save and load not currently working
# @when('save')
# def save():
#    data = {"current_room": current_room, "inventory": inventory}
#    #pickle.dump(data, open("save.p", "wb"))
#    say("Game saved. ")


# @when('load')
# def load():
#   # data = pickle.load(open("save.p", "rb"))
#     global current_room
#    current_room = data["current_room"]
#    global inventory
#    inventory = data["inventory"]
#    say("Game loaded. ")
#    look()
#    show_inventory()

if __name__ == "__main__":
    # look()
    mechanics.testing()
    start()

