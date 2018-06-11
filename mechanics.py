from __future__ import nested_scopes,generators,division, absolute_import,with_statement, print_function,unicode_literals
from builtins import bytes, chr
from future.utils import python_2_unicode_compatible
from io import open

from adventurelib import *
from story import *

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
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


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)

@when('inv')
@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura', magic=None)
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    else:
        say("You cast " + magic)
look()
start()
