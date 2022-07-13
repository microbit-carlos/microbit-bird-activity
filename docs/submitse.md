# Submit your SoundEffects

When we added a speaker to the BBC micro:bit, we wanted to make sure that the
sound feature was as playful and creative as possible. We didn't just want the
micro:bit to beep like your dishwasher; we wanted people to make their
micro:bits squeak like a clanger, chirp like a bird, chatter like R2-D2 or
emote like WALLᐧE. 

To help do this, the
[team at Lancaster University](https://github.com/lancaster-university/codal-microbit-v2/graphs/contributors)
built a synthesizer that would give a lot of creative control over the sounds
the micro:bit made, and also work well in the frequency range that the
micro:bit speaker performs well in (loudest around 2.5kHz, which is very well
aligned with bird song!). 

This Synthesizer was used to make the
[built-in micro:bit sounds](https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html#built-in-sounds-v2),
but until now, we've not exposed the finer grained APIs to users directly.
That's changing, and this exercise uses a preview of those new APIs.

## Built-in Sound Effects

We are in the process of creating the default Sound Effects that will be
included in the micro:bit MicroPython runtime to demonstrate the range of
things people can make with these APIs, and we would love your help!

We're taking submissions from the community for cool sound effects will blow
students minds (or at least, expand them and bring a smile!).

If you have a Sound Effect you'd like to submit you can follow these steps:

- [Fork](https://github.com/microbit-carlos/microbit-bird-activity/fork) the https://github.com/microbit-carlos/microbit-bird-activity/
  repository
- Create a copy of the `template.py` python file in the `sound-effect-examples`
  folder, and give it a new name.
    - This is important so that we can give you credit for your contribution
    - The MicroPython source code is under the MIT license, so using this
      license for the contributions is the easiest option
- Replace the "Your-name-goes-here" placeholder in the copyright line with
  your name
- You can add as many Sound Effects as you like into the same file
- Remember to play them at the bottom of the file
- Submit the PR 

We appreciate every single submission, but as he micro:bit has limited
resources we can only include a few effects in the final, official image.
But don't worry, if we can't include your effect into the MicroPython build,
it will still be available in this repository and they will be showcased in
future versions of this workshop. 
