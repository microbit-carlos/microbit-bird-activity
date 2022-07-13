# Welcome!
# This is the main script for your bird. Some of the functionality is in the
# bird.py file, feel free to have a peek if you like, but there is no need yet.
from microbit import *
import bird

# Your bird will react to events in their environment via decorators like the
# one below this comment. You can modify this example and create new ones for
# all the other events: "hello", "cat", "hawk", "food", "dawn", "dusk"

@bird.react("hello")
def hello():
    """Somebody is saying hi, how lovely!"""
    display.show(Image.HEART)
    sleep(400)

@bird.react("cat")
def cat():
    """ What is that?? I think I just saw a cat!
    Remember to warn the rest of the birds!"""
    pass


# Other things can also happen to our birds, check its state and act accordingly 
while True:
    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    if bird_state == "chill":
        display.show(Image.HAPPY)
    # What other states we can react to in here? Let's try "angry"
    sleep(100)
