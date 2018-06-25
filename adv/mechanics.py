from __future__ import (nested_scopes, generators, division, absolute_import,
                        with_statement, print_function, unicode_literals)

import json

from adventurelib import Room, Item, say, when, Bag, start, set_context
import story

@when('say RESPONSE', context='final_door')
@when('speak RESPONSE', context='final_door')
@when('answer RESPONSE', context='final_door')
def answer(response):
    nb = story.inventory.find("Notebook")
    if nb and nb.letters_found:
        if len(nb.letters_found) == len(story.letter_bank):
            say("You have found all the letters. ")
        # for letter in nb.letters_found:
        #    say(letter)
    say("You speak the words to the door and.... ")
    if response == "THANKS FOR PLAYING".lower():
        say("The door swings open! Thank you for playing!")
    else:
        say("nothing happens")


@when('buy THING', context='shop')
def buy(thing):
    gold = story.inventory.gold
    item = story.shop.items.find(thing)
    if item:
        if item.cost < gold:
            say("you buy the thing")
            story.inventory.gold -= item.cost
            story.inventory.add(item)
        else:
            say("you can't afford the thing")


def matrixTranspose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def Get_Room_List():
    roomlist = []
    for x in story.Room_List:
        roomlist1 = []
        for y in x:
            if y.description:
                if y == story.current_room:
                    roomlist1.append(2)
                else:
                    roomlist1.append(1)
            else:
                roomlist1.append(0)
        roomlist.append(roomlist1)
    ret = roomlist
#    ret = matrixTranspose(roomlist)
#    print(ret)
    with open("../Overlays/room_data.js", "w") as wf:
#    with open("room_data.json", "w") as wf:
        jsonStr = json.dumps(ret)
        # json.dump(ret, wf)
        jsonStr = "var rooms = "+jsonStr+";"
        print(jsonStr)
        wf.write(jsonStr)
    return(ret)


def testing():
    nb = story.inventory.find("Notebook")
    for obj in story.letter_bank:
        nb.letters_found.add(obj)
# inventory.add()


if __name__ == "__main__":
    testing()
    Get_Room_List()
#    start()
