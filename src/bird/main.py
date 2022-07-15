# Welcome!
# This is the main script for your bird. Some of the functionality is in the
# bird.py file, feel free to have a peek if you like, but there is no need yet.
from microbit import *
import bird

# Your bird will react to events in their environment via decorators like the
# one below this comment. You can modify this example and create new ones for
# all the other events: "hello", "cat", "hawk", "dawn", "dusk"

@bird.react("hello")
def hello():
    """Somebody is saying hi, how lovely!"""
    display.show(Image.HEART)
    sleep(400)


# Other things can also happen to our birds, check its mood and act accordingly 
while True:
    # Look inside yourself and listen, how is your bird feeling?
    bird_mood = bird.current_mood()
    if bird_mood == "chill":
        display.show(Image.HAPPY)
    # What other moods we can react to in here? Let's try "angry"

    sleep(200)
