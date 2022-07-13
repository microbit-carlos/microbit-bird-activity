# MicroPython on the BBC micro:bit

Need to add some content here.

Links:
- https://github.com/microbit-foundation/micropython-microbit-v2
- https://microbit-micropython.readthedocs.io/en/v2-docs/

SoundEffect:
- https://github.com/bbcmicrobit/micropython/pull/753
- https://microbit-micropython--753.org.readthedocs.build/en/753/audio.html


## Quick things to do with the micro:bit

#quick-things-to-do-with-the-microbit

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

Create your own sounds! More info here:
https://microbit-micropython--753.org.readthedocs.build/en/753/audio.html

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
