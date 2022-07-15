# MicroPython on the BBC micro:bit

Python is possible in the micro:bit thanks to Damien George's
[MicroPython](https://micropython.org/), and all of its contributors 
([one](https://github.com/bbcmicrobit/micropython/graphs/contributors),
[two](https://github.com/microbit-foundation/micropython-microbit-v2/graphs/contributors),
[three](https://github.com/micropython/micropython/graphs/contributors)). For
a history of how this came to be, Nicholas Tollervey also has a great post
on his blog:
[The Story of MicroPython on the BBC micro:bit](https://ntoll.org/article/story-micropython-on-microbit/)

![MicroPython comic](https://microbit-micropython.readthedocs.io/en/v2-docs/_images/comic.png)

These are useful links to find out how to use MicroPython on the micro:bit:
- [micro:bit MicroPython docs](https://microbit-micropython.readthedocs.io/en/v2-docs/)
- [microbit.org Python User Guide](https://microbit.org/get-started/user-guide/python/)

SoundEffect Information:
- [GitHub PR with proposed user docs](https://github.com/bbcmicrobit/micropython/pull/753)
- [Preview of the docs from the PR](https://microbit-micropython--753.org.readthedocs.build/en/753/audio.html)

The micro:bit V2 MicroPython repository: [https://github.com/microbit-foundation/micropython-microbit-v2](https://github.com/microbit-foundation/micropython-microbit-v2)


## Quick things to do with the micro:bit

To "Reference" left side bar in the editor is the best place to find out more
about the micro:bit features in MicroPython. But for a quick , these are a couple of quick snippets that output sound or images.

Display one of the built-in images (more info [here](https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/images.html)):

```python
from microbit import *

display.show(Image.HAPPY)
```

Play one of the built-in sounds (full list [here](https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html#built-in-sounds-v2)):

```python
from microbit import *

audio.play(Sound.HAPPY)
```

Play one of the built-in music tunes:

```python
import music

music.play(music.BIRTHDAY)
```

Make your own music tune (more info [here](https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/music.html)):

```python
import music

tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
music.play(tune)
```

Speak (more info [here](https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/speech.html)):

```python
import speech

speech.say("Hello, World")
```

Create your own sounds!

More info here:
[Preview of the proposal for the SoundEffect documentation](https://microbit-micropython--753.org.readthedocs.build/en/753/audio.html)

```python
from microbit import *
audio.play(audio.SoundEffect(
    freq_start=400,
    freq_end=2000,
    duration=500,
    vol_start=100,
    vol_end=255,
    wave=audio.SoundEffect.WAVE_TRIANGLE,
    fx=audio.SoundEffect.FX_VIBRATO,
    interpolation=audio.SoundEffect.INTER_LOG
))
```
