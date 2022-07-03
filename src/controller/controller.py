from microbit import *
import radio

options = ['hello', 'cat', 'hawk', 'food', 'dawn', 'dusk']
i = 0
display.show(i)

radio.on()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(options[i])
        display.show(Image.ARROW_N)
        sleep(500)
    elif button_a.is_pressed():
        i = i + 1 if i < (len(options) - 1) else 0
        display.show(i)
        sleep(500)
    elif button_b.is_pressed():
        i = i - 1 if i > 0 else len(options) - 1
        display.show(i)
        sleep(500)
    elif pin0.is_touched():
        display.scroll(options[i])
    display.show(i)
    sleep(100)
