# Bird State Angry

```python
while True:
    # Look inside yourself and listen, how is your bird feeling?
    bird_mood = bird.current_mood()
    if bird_mood == "chill":
        display.show(Image.HAPPY)
    elif bird_mood == "angry":
        display.show(Image.ANGRY)

    sleep(100)
```