from microbit import *
import random
import radio


msg_options = ["hello", "cat", "hawk", "food", "dawn", "dusk"]
active_birds = dict({
    "fake_bird": running_time()
})
MSG_DELIMITER = "->"


def check_birds():
    """
    Infinite Generator, to be called at an interval to keep asking active birds
    to say hi, so that we know they are still active.
    """
    global active_birds
    while True:
        active_birds_copy = active_birds.copy()
        # First confirm all active birds still present
        for bird_id in active_birds_copy.keys():
            print("👀 Check bird presence: {}".format(bird_id))
            radio_send_group("hello", bird_id)
            yield


bird_check = check_birds()
#@run_every(s=30)
@run_every(s=10)
def check_next_bird():
    # First say hello to the next bird in the list
    next(bird_check)
    # Then purge birds we have not heard from in a long time
    global active_birds
    birds = list(active_birds.keys())
    deadline = running_time() - (len(birds) * 3 * 60 * 1000)
    for bird_id in birds:
        if active_birds[bird_id] < deadline:
            print("❗️ Haven't heard from bird {} in over {} min, ".format(
                bird_id, deadline // 60000) + "must have flown away.")
            del active_birds[bird_id]


def radio_send_group(msg, send_to="all"):
    """
    After a bird is register with the hello message it switches to group 17
    So, messages go out in group 17, but all other operations are in group 1.

    :param msg: The message (from msg_options[]) to send out.
    :param send_to: Bird ID to send to a single bird, "all" to send to all the
                    birds, or a falsy value to send to a random bird.
    """
    radio.config(group=17, power=7)
    if not send_to:
        global active_birds
        bird_list = list(active_birds.keys())
        if bird_list:
            send_to = random.choice(bird_list)
        else:
            print("No active birds to pick, sending to all.")
            send_to = "all"
    msg = "{}{}{}".format(msg, MSG_DELIMITER, send_to)
    print("radio send: {}".format(msg))
    radio.send(msg)
    radio.config(group=1, power=7)


def reset_all():
    """Sends a reset message to all birds and clears the active list."""
    global active_birds
    active_birds.clear()
    radio_send_group("reset", send_to="all")


# Turn on the radio and set group 1 to listen for new birds
radio.on()
radio.config(group=1, power=7)

print("🚀 Programme starting...")
#reset_all()
i = 0
while True:
    # Listen for new birds
    radio_received = None
    try:
        radio_received = radio.receive()
    except:
        print("Error receiving msg: {}".format())
    else:
        if radio_received:
            print("🐦 Bird heard: {}".format(radio_received))
            msg_split = radio_received.split(MSG_DELIMITER)
            if len(msg_split) != 2:
                print("Could not separate msg into two.")
            else:
                if msg_split[0] == "hello":
                    # Add new entry or update timestamp to indicate the last
                    # time we heard from this bird
                    active_birds[msg_split[1]] = running_time()
                    # Send message back to let the bird know it's registered
                    radio.send(radio_received)
                else:
                    print("Unexpected msg start: {}".format(msg_split[0]))

    # Use buttons to select message to send out
    if button_a.is_pressed() and button_b.is_pressed():
        # A & B send a message out
        if pin0.is_touched():
            # pin0 pressed for the message to be sent to a single random bird
            display.show("R")
            radio_send_group(msg_options[i], send_to=False)
        else:
            # pin0 not touch to send message to all birds
            display.show("A")
            radio_send_group(msg_options[i], send_to="all")
        sleep(500)
    elif button_a.is_pressed():
        # Button A to decrease selection
        i = i - 1 if i > 0 else len(msg_options) - 1
        display.show(i)
        sleep(500)
    elif button_b.is_pressed():
        # Button B to increase selection
        i = i + 1 if i < (len(msg_options) - 1) else 0
        display.show(i)
        sleep(500)
    elif pin2.is_touched():
        # Scroll the message on the display when pin2 is touched
        display.scroll(msg_options[i])
    # Update the selection on the display and wait before the next iteration
    display.show(i)
    sleep(200)
