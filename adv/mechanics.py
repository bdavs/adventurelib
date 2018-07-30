from __future__ import (nested_scopes, generators, division, absolute_import,
                        with_statement, print_function, unicode_literals)

import json
import os
# from adventurelib import Room, Item, say, when, Bag, start, single_command, prompt, get_output
import adventurelib as adv
from adventurelib import when
import story


# this should be a testing function only
@when('give ITEM')
def give(item):
    if adv.TESTING:
        thisItem = story.master_item_list.find(item)
        if thisItem:
            story.inventory.add(thisItem)
            adv.say("Added {} to your bag".format(thisItem))
        else:
            adv.say("Sorry could not find that item")
    else:
        adv.say("Sorry, that feature is not currently enabled")

@when('say RESPONSE', context='final_door')
@when('speak RESPONSE', context='final_door')
@when('answer RESPONSE', context='final_door')
def answer(response):
    nb = story.inventory.find("Notebook")
    if nb and nb.letters_found:
        if len(nb.letters_found) == len(story.letter_bank):
            adv.say("You have found all the letters. ")
        # for letter in nb.letters_found:
        #    adv.say(letter)
    adv.say("You speak the words to the door and.... ")
    if response == "THANKS FOR PLAYING".lower():
        adv.say("The door swings open! You walk into the light with a satisfaction of completing your quest. Thank you for playing!")
    else:
        adv.say("nothing happens :-( Try again.")


@when('buy THING', context='shop')
@when('purchase THING', context='shop')
def buy(thing):
    gold = story.inventory.gold
    item = story.shop_room.store_items.find(thing)
    if item:
        if item.cost <= gold:
            adv.say("You buy the {}. ".format(item))
            story.inventory.gold -= item.cost
            story.shop_room.store_items.take(thing)
            #adv.say("{}".format(story.letter_bank))
            if item in story.letter_bank:
                nb = story.inventory.find("notebook")
                if nb:
                    adv.say('You tape the %s in your notebook' % item)
                    nb.letters_found.add(item)
                else:
                    adv.say("You do not have a way to record it, so you just drop it on the ground")
                    story.current_room.items.add(item)
            else:
                story.inventory.add(item)
            adv.say("You now have {} gold. ".format(story.inventory.gold))
        else:
            adv.say("You can't afford the {}. you have {} gold and it costs {} gold. ".format(item,gold,item.cost))
    else:
        adv.say("Sorry I don't have a {} in my shop. ".format(thing))

        
@when('sell THING', context='shop')
@when('sell', context='shop', thing='')
@when('rob THING', context='shop')
@when('steal THING', context='shop')
def sell(thing):
    adv.say("I ain't no fool or a charity, kid. Go find your own way to make some money like the rest of us.")


        
def matrixTranspose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

room_status = {"current": 2, "visited": 1,"seen":3, "unseen": 0, "nonexistant":0 }
def Get_Room_List():
    roomlist = []
    for x in story.Room_List:
        roomlist1 = []
        for y in reversed(x):
            if y.description:
                if y == story.current_room:
                    roomlist1.append(room_status["current"]) # current room
                elif y.visited == room_status["visited"]:
                    roomlist1.append(room_status["visited"]) # room visited
                elif y.visited == room_status["seen"]:
                    roomlist1.append(room_status["seen"]) # room seen
                else:
                    roomlist1.append(room_status["unseen"]) # room not seen
            else:
                roomlist1.append(room_status["nonexistant"]) # room nonexistant
        roomlist.append(roomlist1)
    ret = roomlist
#    ret = matrixTranspose(roomlist)
#    print(ret)
    #directory = os.path.dirname(__file__)
    #with open(directory+"/../Overlays/room_data.js", "w") as wf:
#    with open("room_data.json", "w") as wf:
    jsonStr = json.dumps(ret)
        # json.dump(ret, wf)
    #    jsonStrF = "var rooms = "+jsonStr+";"
        # print(jsonStr)
    #    wf.write(jsonStrF)
    return(jsonStr)


def Has_Map():
    haveMap = True if story.inventory.find("Map") else False
    return(haveMap)
    
    
def testing():
    nb = story.inventory.find("Notebook")
    for obj in story.letter_bank:
        nb.letters_found.add(obj)
    story.inventory.add(story.compass)
# inventory.add()


if __name__ == "__main__":
    testing()
    while True:
        cmds = raw_input(adv.prompt())
        adv.single_command(cmds)
        print(adv.get_output())
        Get_Room_List()
#    start()
