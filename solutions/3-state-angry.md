# Bird State Angry

```python
while True:
    # Look inside yourself and listen, how is your bird feeling?
    bird_state = bird.current_state()
    if bird_state == "chill":
        display.show(Image.HAPPY)
    elif bird_state == "angry":
        display.show(Image.ANGRY)

    sleep(100)
```