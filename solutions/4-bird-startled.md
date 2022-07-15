# Adding A New Bird Mood: `startled`

```python
def current_mood():
    # Check for motion
    if __mb.accelerometer.was_gesture('shake'):
        return 'angry'
    # Check for a loud noise
    if __mb.microphone.was_event() == __mb.SoundEvent.LOUD:
        return 'startled'

    __mb.sleep(10)   # Ensure run_every/gestures have a chance to run
    return "chill"
```
