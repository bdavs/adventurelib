# adventurelib

`adventurelib` provides basic functionality for writing text-based adventure games

The foundation of adventurelib is the ability to define functions that are
called in response to commands. For example, you could write a function to
be called when the user types commands like "take hat":

    @when('take THING')
    def take(thing):
        print(f'You take the {thing}.')
        inventory.append(thing)

It also includes the foundations needed to write games involving rooms, items,
characters and more... but users will have to implement these features for
themselves as they explore Python programming concepts.

## Installing

This may be used from the python script itself (starting in story.py)

or it will work in Streamlabs Chatbot as a script

## Documentation

[Comprehensive documentation is on Read The Docs.](http://adventurelib.readthedocs.io/)
