from microbit import *
import bird
import audio_soundeffect as audio

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