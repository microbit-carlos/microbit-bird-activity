# Say "hello" to all birds via radio

bird.py:

```python
def say_hello_to_everyone():
    # Impose a delay before warning others
    __mb.sleep(__rand.randint(500,1500))
    __radio.send("hello->all")
```

main.py

```python
while True:
    if button_a.is_pressed():
        bird.say_hello_to_everyone()
        sleep(500)

    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    ...
```
