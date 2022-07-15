## Solution 1: Hello event - Beating heart

Exercise:

Birds can be very chatty, so your neighbours might be saying hello quite often.
Can you think of a way to alternate between showing `Image.HEART` and
`Image.HEART_SMALL`? That way it'll look like a beating heart!

```python
BIG_HEART = True

@bird.react("hello")
def hello():
    """Somebody is saying hi, how lovely!"""
    # Toggle the display between small and large heart
    global BIG_HEART
    display.show(Image.HEART if BIG_HEART else Image.HEART_SMALL)
    BIG_HEART = not BIG_HEART
```
