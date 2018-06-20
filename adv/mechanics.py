from __future__ import (nested_scopes, generators, division, absolute_import,
with_statement, print_function, unicode_literals)


from adventurelib import Room, Item, say, when, Bag, start, set_context, get_context
import story


@when('answer RESPONSE') #, context='final_door', magic=None)
def answer(response):
    nb = story.inventory.find("Notebook")
    if nb and nb.letters_found:
        if len(nb.letters_found) == len(story.letter_bank):
            say("\\me You have found all the letters. ")
        #for letter in nb.letters_found:
        #    say(letter)
    say("You speak the words to the door and.... ")
    if response == "THANKS FOR PLAYING".lower():
        say("The door swings open! Thank you for playing!")
    else:
        say("nothing happens")

def testing():
    nb = story.inventory.find("Notebook")
    for obj in story.letter_bank:
        nb.letters_found.add(obj)
    #inventory.add()

if __name__ == "__main__":
    testing()
    start()