# microbit-module: bird@0.0.1
import radio as __radio
import microbit as __mb

__radio.config(group=7)
__radio.on()
__radio.send('hello')

def __wait_for_start():
    while True:
        message = __radio.receive()
        if message == "start":
            return
            
_radio_messages = ['hello', 'cat', 'hawk', 'food', 'dawn', 'dusk']

normal = "hello"

def process_world():
    '''
    This is the bird's brain, processing the world around.
    The bird knows several 'actions' that can happen as a result of thinking
     - hello: new bird has arrived in the flock
     - cat : predator below
     - hawk: predator above
     - food: time for dinner
     - dawn: time to wake up
     - dusk: time to go to sleep
     - squawk: something loud happened
     - motion: some kind of movement happened
     - chill: nothing is happening, rest
     - ...extend your bird by editing the bird.py file!
    
    :return: action (str): one of the possible actions for the bird
    '''
    # Check for radio signals:
    # for us/under the hood: 
        # stop
        # start
    # for the user:
        # hello: new bird
        # cat : predator below
        # hawk: predator above
        # food: time for dinner
        # dawn: time to wake up
        # dusk: time to go to sleep
    message = __radio.receive()
    if message:
        if message == "stop":
            #sleep!
            #while we don't have sleep, just loop waiting for the start command
            __wait_for_start()
        elif (message == "hawk"  or message == "cat"):
            #impose a small delay before warning others
            __mb.sleep(200)
            return message
        else:
            if message in _radio_messages:
                return message
    # Check for a loud noise
    if __mb.microphone.current_event() == __mb.SoundEvent.LOUD:
        return 'squawk'
    # Check for motion
    if __mb.accelerometer.was_gesture('shake'):
        return 'motion'
    return "chill"

def warn_about_hawk():
    __radio.send("hawk")

def warn_about_cat():
    __radio.send("cat")