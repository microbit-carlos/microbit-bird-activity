# Say Hello to a specific neighbour

bird.py:

```python
def say_hello_to(friendly_name):
    # Impose a delay before warning others
    __mb.sleep(__rand.randint(500,1500))
    __radio.send("hello->{}".format(friendly_name))
```

main.py

```python
while True:
    if button_a.is_pressed():
        # Find out somebody else friendly name
        bird.say_hello_to("friendly name goes here")
        sleep(500)
    elif button_b.is_pressed():
        my_name = bird.friendly_name()
        display.scroll(my_name)
        print("My bird name is: {}".format(my_name))

    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    ...
```
