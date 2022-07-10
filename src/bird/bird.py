# microbit-module: bird@0.0.1
import radio as __radio
import microbit as __mb
import machine as __machine
import struct as __struct
import random as __rand

BIRD_NAME = None
MSG_DELIMITER = "->"
RADIO_GROUP_HELLO = 1
RADIO_GROUP_BIRDS = 17

# Defined radio messages to react to
_events = ['hello', 'cat', 'hawk', 'food', 'dawn', 'dusk']
_states = ["chill", "hungry", "angry"]

# Callbacks for the react decorator
__event_callbacks = {}

def react(function, radio_event):
    """Decorator to register function callbacks for radio messages."""
    if radio_event in _events:
        __event_callbacks[radio_event] = function
    else:
        raise Exception("Invalid message registered via @react decorator.")
    return function


def __hi_everyone_i_am_here():
    """Say hello to the world until you hear hello back to you.
    The micro:bit that transmits radio events keeps a list of active birds,
    so this is a way to register your bird is active.
    """
    print("Hello, my name is {}. Can anybody hear me...?".format(BIRD_NAME))
    __radio.config(group=RADIO_GROUP_HELLO, power=7)
    __radio.on()
    msg_out = "hello{}{}".format(MSG_DELIMITER, BIRD_NAME)
    timeout = __mb.running_time() + (60 * 1000)
    while __mb.running_time() < timeout:
        try:
            __radio.send(msg_out)
            __mb.sleep(__rand.randint(100,200))
            radio_received = __radio.receive()
        except:
            pass
        else:
            if radio_received == msg_out:
                # So glad somebody finally said hello back, it was getting kind of rude
                # I can go on my business now
                print("🎉 Somebody said hello back, this is such a friendly neighbourhood!")
                break
    else:
        # I've been waiting too long to be acknowledged
        print("Warning! Bird could not hear any hello back.")
    # Move to the radio group with all the birds
    __radio.config(group=RADIO_GROUP_BIRDS, power=0)


def __friendly_name():
    length, letters = 5, 5
    codebook = [
        ['z', 'v', 'g', 'p', 't'],
        ['u', 'o', 'i', 'e', 'a'],
        ['z', 'v', 'g', 'p', 't'],
        ['u', 'o', 'i', 'e', 'a'],
        ['z', 'v', 'g', 'p', 't']
    ]
    name = []
    # Derive our name from the unique ID
    _, n = __struct.unpack("II", __machine.unique_id())
    ld = 1;
    d = letters;
    for i in range(0, length):
        h = (n % d) // ld;
        n -= h;
        d *= letters;
        ld *= letters;
        name.insert(0, codebook[i][h]);
    return "".join(name);


@__mb.run_every(s=2)
def __check_radio_msgs():
    try:
        message = __radio.receive()
    except:
        print("There was an error reading radio")
        return
    try:
        #process_world(message)
        pass
    except:
         print("There was an error processing the world")


def process_world(message):
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
    if message:
        if message == "stop":
            #sleep!
            #while we don't have sleep, just loop waiting for the start command
            #__wait_for_start()
            pass
        elif (message == "hawk"  or message == "cat"):
            #impose a small delay before warning others
            __mb.sleep(200)
            return message
        else:
            if message in _events:
                return message
    # Check for a loud noise
    if __mb.microphone.current_event() == __mb.SoundEvent.LOUD:
        return 'squawk'
    # Check for motion
    if __mb.accelerometer.was_gesture('shake'):
        return 'motion'
    __mb.sleep(10)   # Ensure run_every has a chance to run
    return "chill"


def warn_about_hawk():
    __radio.send("hawk")


def warn_about_cat():
    __radio.send("cat")


def __init():
    global BIRD_NAME
    BIRD_NAME = __friendly_name()
    __hi_everyone_i_am_here()


# We run some init code on import
__init()
