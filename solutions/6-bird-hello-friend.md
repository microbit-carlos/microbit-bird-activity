# Say Hello to a specific neighbour

bird.py:

```python
def say_hello_to(friendly_name):
    __radio.send("hello->{}".format(friendly_name))
```

main.py

```python
while True:
    if button_a.is_pressed():
        # Find out somebody else friendly name
        bird.say_hello_to("friendly name goes here")
        # Wait a bit to ensure a single press doesn't trigger multiple hellos
        sleep(500)
    elif button_b.is_pressed():
        my_name = bird.friendly_name()
        display.scroll(my_name)
        print("My bird name is: {}".format(my_name))

    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    ...
```
