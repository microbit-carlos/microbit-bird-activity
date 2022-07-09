from microbit import *
import random
import radio


options = ['hello', 'cat', 'hawk', 'food', 'dawn', 'dusk']
active_birds = set(['carlos'])
MSG_DELIMITER = "->"


def check_birds():
    """
    Infinite Generator, to be called at an interval to keep the list
    of active birds up to date.
    """
    global active_birds
    while True:
        active_birds_copy = active_birds.copy()
        # First confirm all active birds still present
        for bird_id in active_birds_copy:
            send_msg = "hello{}{}".format(MSG_DELIMITER, bird_id)
            radio.send(send_msg)
            timeout = running_time() + 2500
            while running_time() < timeout:
                try:
                    radio_msg = radio.receive()
                except:
                    pass
                else:
                    if radio_msg == send_msg:
                        break
                finally:
                    yield
            else:
                # We get here on timeout without a response
                active_birds.remove(bird_id)


def radio_send_group(msg, send_to_all=True):
    """
    After a bird is register it switches to group 1
    So, messages out go to group 1
    """
    global active_birds
    bird_list = list(active_birds)
    radio.config(group=1)
    print("Radio send to {}: {}".format(
        "all" if send_to_all else "random", msg
    ))
    bird = "all"
    if not send_to_all:
        if bird_list:
            bird = random.choice(bird_list)
        else:
            print("No registered birds to pick.")
    msg = "{}{}{}".format(msg, MSG_DELIMITER, bird)
    print("radio send: {}".format(msg))
    radio.send(msg)
    radio.config(group=0)


def reset_all():
    """Sends a reset message and clears the list of active birds."""
    global active_birds
    active_birds.clear()
    radio_send_group("reset", send_to_all=True)


# Turn on the radio and set group 0 to listen for new birds
radio.on()
radio.config(group=0)

reset_all()

i = 0
while True:
    # Listen for new birds
    radio_received = None
    try:
        radio_received = radio.receive()
    except:
        print("error receiving message on group 0: {}".format())
    else:
        if radio_received:
            print("bird heard: {}".format(radio_received))
            msg_split = radio_received.split(MSG_DELIMITER)
            if len(msg_split) != 2:
                print("Could not separate message into 2")
            else:
                if msg_split[0] == "hello":
                    active_birds.add(msg_split[1])
                    # Send message back to let the bird know it's registered
                    radio.send(radio_received)
                else:
                    print("Unexpected msg start: {}".format(msg_split[0]))

    # Check buttons to see if we need to send something out
    if button_a.is_pressed() and button_b.is_pressed():
        if pin0.is_touched():
            display.show("R")
            radio_send_group(options[i], send_to_all=False)
        else:
            display.show("A")
            radio_send_group(options[i], send_to_all=True)
        sleep(500)
    elif button_a.is_pressed():
        i = i - 1 if i > 0 else len(options) - 1
        display.show(i)
        sleep(500)
    elif button_b.is_pressed():
        i = i + 1 if i < (len(options) - 1) else 0
        display.show(i)
        sleep(500)
    elif pin2.is_touched():
        display.scroll(options[i])
    display.show(i)
    sleep(200)
