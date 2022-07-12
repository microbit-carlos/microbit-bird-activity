# It's alive

Let's bring our bird alive with code!

## What is all this about?

Your task is to think like a bird and programme the micro:bit to react to the world like a bird.

The micro:bit can communicate wirelessly with other micro:bits using radio.
There will be a secret micro:bit in the room broadcasting radio messages to
all the birds indicating different events like "saying hello" o "there is a cat
around".

Apart from that the micro:bit contains other sensors that your bird will react
to, for example, birds don't like to be shaken!

## First steps - load the starter project into the editor

Okay, so the first step is to open this link to the Python Editor.
This link contains a flag to enable additional beta features:
[https://python.microbit.org/v/beta?flag=audioSoundEffect](https://python.microbit.org/v/beta?flag=audioSoundEffect)

To start the activity we first need to load a project hex file into the editor
with some starter code.

Right click on this link and select "Save Link As" to save the hex file to your
laptop: [https://github.com/microbit-carlos/microbit-bird-activity/raw/main/src/bird/bin/flockbird.hex](https://github.com/microbit-carlos/microbit-bird-activity/raw/main/src/bird/bin/flockbird.hex)

And then drag and drop the hex file to the Python Editor. The editor might
warn you that this action will replace the project, you can click "Replace" to
accept it.

### So... What is all this?

Okay, so this hex file contains two files, to see them let's go to "Project"
section on the left sidebar:

![Python Editor Projects](img/editor-project.png)

In this view you can switch between the `main.py` file and the `bird.py`.

- The `bird.py` module contains some functionality for the bird to be able to
react to the world.
- The `main.py` file is the main code we will be working on.

There are some comments in both files that should help clarify what things
are doing, but you can continue with the activity as we look at different
parts in steps.


## TODO

Things that will be included here:
- Quick overview of the micro:bit
- Explanation that the bird reacts to things in the environment (radio
  messages) and physical state (shaken, loud)
- Activity 1: Expand the events (decorator function) to react to something else
- Activity 2: Expand the state (if-else inside `while True`)to react to something
- Explain there are also a new Sound Effect system and provide example
- Activity 3: Create a new sound for any of the reactions/states
- Show that the Python project has a bird.py and main.py file 
- Activity 4: Create a new event or state in bird.py, then react to it in main.py
- What else?
