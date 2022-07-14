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
    audio.play(Sound.HAPPY)
    sleep(400)

@bird.react("cat")
def cat():
    """ What is that?? I think I just saw a cat!
    Remember to warn the rest of the birds!"""
    display.show(Image.GIRAFFE)
    audio.play(Sound.SLIDE)
    bird.warn_about_cat()

@bird.react("hawk")
def hawk():
    display.show(Image.BUTTERFLY)
    audio.play(Sound.MYSTERIOUS)
    bird.warn_about_hawk()

@bird.react("dawn")
def dawn():
    display.show(Image.ASLEEP)
    audio.play(Sound.YAWN)

@bird.react("dusk")
def dusk():
    display.show(Image.CONFUSED)
    audio.play(Sound.SPRING)

# Other things can also happen to our birds, check its mood and act accordingly 
while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_N)
        # Find out somebody else friendly name
        bird.say_hello_to("all")
        # Wait a bit to ensure a single press doesn't trigger multiple hellos
        sleep(500)
    elif button_b.is_pressed():
        my_name = bird.friendly_name()
        print("🏷 My bird name is: {}".format(my_name))
        display.scroll(my_name)

    # Look inside yourself and listen, how is your bird feeling?
    bird_mood = bird.current_mood()
    if bird_mood == "chill":
        display.show(Image.HAPPY)
    elif bird_mood == "angry":
        display.show(Image.ANGRY)
    # What other moods we can react to in here? Let's try "angry"
    sleep(100)
