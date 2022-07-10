# Welcome!
# This is the main script for your bird. Some of the functionality is in the
# bird.py file, feel free to have a peek if you like, but there is no need yet.
from microbit import *
import bird
import audio_soundeffect as audio

# Your bird will react to events in their environment via decorators like the
# one below this comment. You can modify this example and create new ones for
# all the other events:
# TODO: copy the final list here

BIG_HEART = True

@bird.react("hello")
def hello():
    """Somebody is saying hi, how lovely!"""
    # Toggle the display between small and large heart
    global BIG_HEART
    display.show(Image.HEART if BIG_HEART else Image.HEART_SMALL)
    BIG_HEART = not BIG_HEART

@bird.react("cat")
def cat():
    """ What is that?? I think I just saw a cat!
    Remember to warn the rest of the birds!"""
    pass


# But first, let's start reacting to 
while True:
    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    if bird_state == "chill":
        display.show(Image.HAPPY)
    elif bird_state == "angry":
        display.show(Image.ANGRY)
    sleep(100)
