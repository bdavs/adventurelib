from adventurelib import *

Room.items = Bag()

current_room = starting_room = Room("You are in a dark room.")

valley = starting_room.north = Room("""
You are in a beautiful valley.
""")

magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.
""")

mallet = Item('rusty mallet', 'mallet')
valley.items = Bag({mallet,})

inventory = Bag()
