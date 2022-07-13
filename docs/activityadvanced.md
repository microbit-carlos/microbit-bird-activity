# Advanced steps

TODO: Intro


## Expanding the states

TODO: Intro

Look at `bird.py`, find the `current_state()` function:

```python
def current_state():
    # Check for motion
    if __mb.accelerometer.was_gesture('shake'):
        return 'angry'
    # How would you create a new "I fell down" event?
    # A list of gestures can be found in the docs:
    # https://microbit-micropython.readthedocs.io/en/v2-docs/accelerometer.html

    __mb.sleep(10)   # Ensure run_every/gestures have a chance to run
    return "chill"
```

<p class="exercise">
Exercise: <br>
Birds can be noisy, but they don't like loud sounds themselves!
The micro:bit has a microphone, and we can use it to detect loud noises,
so let's create a new state: "startled".
<br>
Let's add another if statement inside the
<code class="language-plaintext highlighter-rouge">current_state()</code>
function in the <code class="language-plaintext highlighter-rouge">bird.py</code> 
file.
And if there was a "loud" event the function returns the `startled` state.

You can find more info about the microphone in the <a href="https://microbit-micropython.readthedocs.io/en/v2-docs/microphone.html" target="_blank">Microphone documentation</a>.
</p>

[Solution](https://github.com/microbit-carlos/microbit-bird-activity/tree/main/solutions/4-bird-startled.md)

Now make a noise near the microphone and see your bird get startled!

Hint: If the conference area is too loud, you can blow on the microphone.


## Sending a Hello radio message

TODO: Into

Let's look at the `warn_about_cat()` function towards the bottom of the
`bird.py` file:

```python
def warn_about_cat():
    # Impose a delay before warning others
    __mb.sleep(__rand.randint(500,1500))
    __radio.send("cat->all")
```

Here we can see two thing:

1. A delay for a random amount of time between 500 milliseconds to 1.5 seconds.
2. Sending the `cat->all` radio message

<p class="exercise">
Exercise: <br>
Let's create a new function in
<code class="language-plaintext highlighter-rouge">bird.py</code>
that says "hello" to all the birds nearby. This will be very similar to the
<code class="language-plaintext highlighter-rouge">warn_about_cat()</code>
function.

Now, in the 
<code class="language-plaintext highlighter-rouge">while True:</code>
loop, let's call the new bird function when
<code class="language-plaintext highlighter-rouge">button_a</code>
is pressed, and you will be able to see the other birds react to your
"Hello" by pressing the button.
</p>

Hint: You might need to add a small delay after saying hello, or you can end
up sending a lot of hello messages around on a single button press.

[Solution](https://github.com/microbit-carlos/microbit-bird-activity/tree/main/solutions/5-bird-hello-everyone.md)

### Say hello to a specific neighbour

The format of these radio messages is very simple: `event->target`
- `event` is the name of the event
- `target` is the "friendly name" of the micro:bit (unique to each board),
  or "all" to send to everyone

So you can send a "hello" message to a specific bird, but how do you find out
the "friendly name" of a micro:bit? 

<p class="exercise">
Exercise: <br>
The friendly name can be obtained using the `bird.friendly_name()` function.
Let's update the code to scroll the friendly name on the display (
<code class="language-plaintext highlighter-rouge">display.scroll()</code>
) when the B button is pressed.
</p>

<p class="exercise">
Exercise: <br>
The friendly name can be obtained using the `bird.friendly_name()` function.
Let's update the code to scroll the friendly name on the display (
<code class="language-plaintext highlighter-rouge">display.scroll()</code>
) when the B button is pressed.
</p>

For the next part you can find a friend on your table to do this together,
or ask one of the micro:bit helpers to get a "neighbour micro:bit".

<p class="exercise">
Exercise: <br>
Can you update your "Say hello to all" function to take a "friendly name" as
and argument and send the message only to that bird?

Then we can update the code that runs when button B is pressed to say hello
to your friend!
</p>

[Solution](https://github.com/microbit-carlos/microbit-bird-activity/tree/main/solutions/6-bird-hello-friend.md)

