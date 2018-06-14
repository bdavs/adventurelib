from __future__ import nested_scopes,generators,division, absolute_import,with_statement, print_function,unicode_literals
from builtins import bytes, chr
from future.utils import python_2_unicode_compatible
from io import open

import pickle

from adventurelib import *

rooms = {}
Room.items = Bag()

#locations
current_room = starting_room = Room("You are in a dark room.")

valley = starting_room.north = Room("""
You are in a beautiful valley.
""")

magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.
""")

wizard_chamber = magic_forest.north = Room("""
You are in a cranky wizard chambers.
""")

tower = wizard_chamber.west = Room("""
You are in a spacious tower.
""")

#items in locations
mallet = Item('rusty mallet', 'mallet')
spoon = Item('greasy spoon', 'spoon')
valley.items = Bag({mallet,spoon,})

wand = Item('wand','wand')
wizard_chamber.items = Bag({wand,})

ball = Item('Crystal ball', 'ball')
tower.items = Bag({ball,})
inventory = Bag()

#action functions
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
        if room == magic_forest:
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
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)

@when('use ITEM')
def use(item):
   current_item = inventory.find(item)
   if not current_item:
       say("you do not have that item")
   elif current_item is ball:
      say(current_room.exits())







@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

#@when('')
@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)

@when('inv')
@when('inventory')
def show_inventory():
    single = True
    say('You have: ')
    for thing in inventory:
        if single:
            say(thing)
            single = False
        else:
            say(", "+str(thing))

@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura', magic=None)
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    else:
        say("You cast " + magic)

@when('save')
def save():
    data = {"current_room": current_room, "inventory":inventory}
    pickle.dump(data, open("save.p","wb"))
    say("Game saved. ")
@when('load')
def load():
    data = pickle.load(open("save.p","rb"))
    global current_room
    current_room = data["current_room"]
    global inventory
    inventory = data["inventory"]
    say("Game loaded. ")
    look()
    show_inventory()
look()
start()
