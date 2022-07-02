# Imports go at the top
from microbit import *
import bird
import music

def pitch_sweep():
    for i in range(4000,5000,50):
        music.pitch(i)
        sleep(10)
    music.pitch(0)

# Code in a 'while True:' loop repeats forever
while True:
    action = bird.process_world()
    # process world could return any of:
    if action == "chill":
        display.show(Image.HEART)    
    elif action == "hello":
        pass 
    elif action == "cat":
        # warn the 
        bird.warn_about_cat() 
    elif action == "hawk":
        # Warn the other birds!
        bird.warn_about_hawk() 
    elif action == "food":
        pass
    elif action == "dawn":
        pass
    elif action == "dusk":
        pass
    elif action == "motion":
        pass
    elif action == "squawk":
        pass        